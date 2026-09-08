"""离线测试：验证调用流程与失败边界，不验证模型质量。"""
import argparse
import contextlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'examples'))
import astra


def completed(text='完成', annotations=None):
    return {'status': 'completed', 'output': [
        {'type': 'reasoning', 'summary': []},
        {'type': 'message', 'content': [{'type': 'output_text', 'text': text,
                                      'annotations': annotations or []}]}]}


class ExamplesTest(unittest.TestCase):
    def args(self, mode, **kwargs):
        return argparse.Namespace(mode=mode, effort='low', max_output_tokens=4096,
                                  prompt=kwargs.get('prompt'), image=kwargs.get('image'))

    def test_extract_schema_nullable_and_strict(self):
        fmt = astra.build_request(self.args('extract'))['text']['format']
        self.assertTrue(fmt['strict'])
        item = fmt['schema']['properties']['items']['items']
        self.assertFalse(item['additionalProperties'])
        self.assertIn('null', item['properties']['deadline']['type'])
        self.assertEqual(set(item['required']), set(item['properties']))

    def test_vision_roundtrip_and_dry_run_redaction(self):
        import base64
        path = Path(__file__).resolve().parents[1] / 'assets/screenshots/workshop-budget.png'
        req = astra.build_request(self.args('vision', image=str(path)))
        url = req['input'][0]['content'][1]['image_url']
        self.assertEqual(base64.b64decode(url.split(',', 1)[1]), path.read_bytes())
        output = io.StringIO()
        with patch.object(astra, 'call_api') as call, contextlib.redirect_stdout(output):
            self.assertEqual(astra.main(['vision', '--image', str(path), '--dry-run']), 0)
            call.assert_not_called()
        self.assertNotIn('data:image', output.getvalue())

    def test_vision_rejects_missing_or_unsupported_input(self):
        with self.assertRaisesRegex(ValueError, '--image'):
            astra.build_request(self.args('vision'))
        with self.assertRaisesRegex(ValueError, 'PNG'):
            astra.build_request(self.args('vision', image='document.pdf'))

    def test_research_citations_and_reasoning_item(self):
        cite = {'type': 'url_citation', 'url': 'https://developers.openai.com/', 'title': '官方'}
        text, citations = astra.read_output(completed('结果', [cite, cite]))
        self.assertEqual(text, '结果')
        self.assertEqual(citations, [('官方', 'https://developers.openai.com/')])

    def test_incomplete_is_not_success(self):
        response = completed('部分结果')
        response.update(status='incomplete', incomplete_details={'reason': 'max_output_tokens'})
        with self.assertRaisesRegex(ValueError, 'max_output_tokens'):
            astra.read_output(response)

    def test_refusal_and_empty_output(self):
        with self.assertRaisesRegex(ValueError, '拒绝'):
            astra.read_output({'status': 'completed', 'output': [{'type': 'message', 'content': [{'type': 'refusal', 'refusal': '原因'}]}]})
        with self.assertRaisesRegex(ValueError, '没有收到'):
            astra.read_output({'status': 'completed', 'output': []})

    def test_no_key_no_network(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(astra, 'call_api') as call, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(astra.main(['text']), 1)
            call.assert_not_called()

    def test_all_text_dry_runs_do_not_call_api(self):
        for mode in ('text', 'research', 'extract'):
            with self.subTest(mode=mode), patch.object(astra, 'call_api') as call, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(astra.main([mode, '--dry-run']), 0)
                call.assert_not_called()

    def test_invalid_budget(self):
        with patch.object(astra, 'call_api') as call, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(astra.main(['text', '--max-output-tokens', '0']), 1)
            call.assert_not_called()

    def test_request_transport(self):
        result = io.BytesIO(json.dumps(completed()).encode())
        with patch('urllib.request.urlopen', return_value=result) as urlopen:
            self.assertEqual(astra.call_api({'model': 'gpt-6-astra'}, 'test-placeholder')['status'], 'completed')
            request = urlopen.call_args.args[0]
            self.assertEqual(request.full_url, astra.ENDPOINT)
            self.assertEqual(request.get_method(), 'POST')
            self.assertEqual(request.get_header('Authorization'), 'Bearer test-placeholder')

    def test_mock_success_saves_output_without_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'result.json'
            with patch.dict(os.environ, {'OPENAI_API_KEY': 'test-placeholder'}), patch.object(astra, 'call_api', return_value=completed('{"items": []}')) as call, contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(astra.main(['extract', '--output', str(path)]), 0)
                self.assertEqual(json.loads(path.read_text())['status'], 'completed')
                self.assertEqual(astra.main(['extract', '--output', str(path)]), 1)
                self.assertEqual(call.call_count, 1)

    def test_http_failure_has_nonzero_exit(self):
        error = urllib.error.HTTPError(astra.ENDPOINT, 429, 'limit', {}, None)
        out = io.StringIO()
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test-placeholder'}), patch.object(astra, 'call_api', side_effect=error), contextlib.redirect_stderr(out):
            self.assertEqual(astra.main(['text']), 1)
        self.assertIn('429', out.getvalue())
        self.assertNotIn('test-placeholder', out.getvalue())


if __name__ == '__main__':
    unittest.main()
