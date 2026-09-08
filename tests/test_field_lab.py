"""Offline checks for the original lab's arithmetic, evidence, and export boundaries."""
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'examples'))
import field_lab as lab
import astra


class FieldLabTests(unittest.TestCase):
    def setUp(self):
        self.brief = json.loads(lab.DEFAULT_BRIEF.read_text())

    def test_budget_and_reserve_are_separate_constraints(self):
        default = lab.evaluate_brief(self.brief)['workshop']
        self.assertEqual((default['spent'], default['remainder']), (2168, 432))
        self.assertTrue(default['reserve_met'])
        changed = lab.evaluate_brief(self.brief, guests=32)['workshop']
        self.assertEqual((changed['spent'], changed['remainder']), (2584, 16))
        self.assertTrue(changed['within_budget'])
        self.assertFalse(changed['reserve_met'])
        self.assertFalse(lab.evaluate_brief(self.brief, budget=2000)['workshop']['within_budget'])

    def test_frames_are_contiguous_and_mismatch_is_visible(self):
        film = lab.evaluate_brief(self.brief)['film']
        self.assertEqual([(s['start_frame'], s['end_frame_exclusive']) for s in film['shots']],
                         [(0, 150), (150, 360), (360, 600)])
        self.assertTrue(film['duration_matches'])
        self.brief['film']['shots'][1]['seconds'] += 1
        self.assertFalse(lab.evaluate_brief(self.brief)['film']['duration_matches'])

    def test_release_requires_all_checks_and_exact_types(self):
        result = lab.evaluate_brief(self.brief)['release']
        self.assertEqual([c['id'] for c in result['checks'] if not c['passed']], ['R02', 'R03'])
        self.assertFalse(result['ready'])
        for check in self.brief['release']['checks']:
            check['observed'] = check['expected']
        self.assertTrue(lab.evaluate_brief(self.brief)['release']['ready'])
        self.brief['release']['checks'][0]['observed'] = 1
        self.assertFalse(lab.evaluate_brief(self.brief)['release']['ready'])

    def test_rejects_invalid_counts_and_duplicate_ids(self):
        for guests in (0, 201, True, '24'):
            with self.subTest(guests=guests), self.assertRaises(ValueError):
                lab.evaluate_brief(self.brief, guests=guests)
        self.brief['film']['shots'][1]['id'] = 'S01'
        with self.assertRaisesRegex(ValueError, 'unique'):
            lab.evaluate_brief(self.brief)

    def test_svg_escapes_input_and_has_no_external_assets(self):
        self.brief['title'] = '<script>& "quoted"'
        result = lab.evaluate_brief(self.brief)
        for render in (lab.render_budget, lab.render_storyboard, lab.render_release):
            svg = render(result)
            tree = ET.fromstring(svg)
            if render != lab.render_storyboard:
                self.assertIn(self.brief['title'], ''.join(tree.itertext()))
            self.assertFalse(any(el.tag.split('}')[-1] in ('script', 'image', 'foreignObject') for el in tree.iter()))
            self.assertNotIn('href=', svg)

    def test_export_roundtrip_and_no_accidental_overwrite(self):
        with tempfile.TemporaryDirectory() as directory, contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(lab.main(['--out', directory]), 0)
            output = Path(directory) / 'results.json'
            self.assertEqual(json.loads(output.read_text())['film']['total_frames'], 600)
            original = output.read_bytes()
            self.assertEqual(lab.main(['--out', directory, '--guests', '32']), 1)
            self.assertEqual(output.read_bytes(), original)
            self.assertEqual(lab.main(['--out', directory, '--guests', '32', '--overwrite']), 0)
            self.assertEqual(json.loads(output.read_text())['workshop']['remainder'], 16)

    def test_committed_vectors_match_generator(self):
        assets = Path(__file__).resolve().parents[1] / 'assets/originals'
        result = lab.evaluate_brief(self.brief)
        for name, render in [('workshop-budget', lab.render_budget), ('craft-storyboard', lab.render_storyboard), ('release-review', lab.render_release)]:
            self.assertEqual((assets / (name + '.svg')).read_text(), render(result))

    def test_invalid_json_writes_no_report(self):
        with tempfile.TemporaryDirectory() as directory, contextlib.redirect_stderr(io.StringIO()):
            source = Path(directory) / 'bad.json'
            source.write_text('{broken')
            out = Path(directory) / 'reports'
            self.assertEqual(lab.main(['--brief', str(source), '--out', str(out)]), 1)
            self.assertFalse(out.exists())

    def test_api_brief_dry_run_includes_data_without_network(self):
        image = Path(__file__).resolve().parents[1] / 'assets/screenshots/workshop-budget.png'
        for args in (['text'], ['vision', '--image', str(image)]):
            output = io.StringIO()
            with patch.object(astra, 'call_api') as call, contextlib.redirect_stdout(output):
                self.assertEqual(astra.main(args + ['--brief', str(lab.DEFAULT_BRIEF), '--dry-run']), 0)
                call.assert_not_called()
            self.assertIn('Paper Circuit Studio', output.getvalue())
            self.assertNotIn('data:image', output.getvalue())

    def test_api_brief_rejects_nonobject_and_oversize_before_network(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(astra, 'call_api') as call, contextlib.redirect_stderr(io.StringIO()):
            source = Path(directory) / 'bad.json'
            for content in ('[]', '{invalid', '{"x":"' + 'a' * 65536 + '"}'):
                source.write_text(content)
                self.assertEqual(astra.main(['text', '--brief', str(source), '--dry-run']), 1)
            call.assert_not_called()
