#!/usr/bin/env python3
"""Astra Responses API 教学示例，Python 3.10+，仅使用标准库。"""
import argparse
import base64
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request

ENDPOINT = 'https://api.openai.com/v1/responses'
EFFORTS = ('low', 'medium', 'high', 'xhigh', 'max')


def build_request(args):
    payload = dict(model='gpt-6-astra', reasoning={'effort': args.effort},
                   max_output_tokens=args.max_output_tokens, store=False)
    if args.mode == 'text':
        payload['input'] = args.prompt or '用三个步骤解释：第一次使用 AI 编程，如何验收生成的代码？'
    elif args.mode == 'vision':
        if not args.image:
            raise ValueError('vision 模式需要 --image 本地图片路径。')
        path = Path(args.image)
        mime = {'.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp'}.get(path.suffix.lower())
        if not mime:
            raise ValueError('请使用 PNG、JPEG 或 WebP 图片。')
        if path.stat().st_size > 10 * 1024 * 1024:
            raise ValueError('本教学示例将图片限制在 10 MB 内，请先缩小图片。')
        encoded = base64.b64encode(path.read_bytes()).decode('ascii')
        payload['input'] = [{'role': 'user', 'content': [
            {'type': 'input_text', 'text': args.prompt or '分析这张截图的组件、布局和可访问性。区分看得见的事实与推测。'},
            {'type': 'input_image', 'image_url': f'data:{mime};base64,{encoded}'},
        ]}]
    elif args.mode == 'research':
        payload['input'] = args.prompt or '查询 OpenAI 官方开发文档中的 GPT-6 Astra 入门方法，给出三条建议与来源链接。标记无法确认的内容。'
        payload['tools'] = [{'type': 'web_search', 'filters': {'allowed_domains': [
            'developers.openai.com', 'platform.openai.com', 'learn.chatgpt.com']}}]
    elif args.mode == 'extract':
        payload['input'] = args.prompt or '从以下模拟会议记录提取行动项，未明确的字段使用 null，不推断日期：小林负责整理首页截图，周五前交付；小周负责检查移动端。'
        payload['text'] = {'format': {
            'type': 'json_schema', 'name': 'action_items', 'strict': True,
            'schema': {'type': 'object', 'additionalProperties': False,
                       'properties': {'items': {'type': 'array', 'items': {
                           'type': 'object', 'additionalProperties': False,
                           'properties': {'task': {'type': 'string'},
                                          'owner': {'type': ['string', 'null']},
                                          'deadline': {'type': ['string', 'null']}},
                           'required': ['task', 'owner', 'deadline']}}},
                       'required': ['items']},
        }}
    return payload


def read_output(response):
    if response.get('status') != 'completed':
        reason = response.get('incomplete_details') or response.get('error') or response.get('status')
        raise ValueError(f'响应未完成：{reason}。检查输出预算或 API 状态。')
    texts, citations = [], []
    for item in response.get('output', []):
        if item.get('type') != 'message':
            continue
        for part in item.get('content', []):
            if part.get('type') == 'refusal':
                raise ValueError('模型拒绝了请求：' + part.get('refusal', '未提供原因'))
            if part.get('type') == 'output_text':
                texts.append(part.get('text', ''))
                for ann in part.get('annotations', []):
                    if ann.get('type') == 'url_citation':
                        citation = (ann.get('title', '来源'), ann['url'])
                        if citation not in citations:
                            citations.append(citation)
    if not any(texts):
        raise ValueError('没有收到文字输出，请检查响应类型或增加输出预算。')
    return '\n'.join(texts), citations


def call_api(payload, key):
    req = urllib.request.Request(ENDPOINT, data=json.dumps(payload).encode('utf-8'),
        headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}, method='POST')
    # 不自动重试，避免超时后重复付费；超时不等于服务器未执行。
    with urllib.request.urlopen(req, timeout=180) as response:
        return json.load(response)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('text', 'vision', 'research', 'extract'))
    parser.add_argument('--prompt', help='替换默认提示词')
    parser.add_argument('--image', help='vision 模式上传的图片')
    parser.add_argument('--effort', choices=EFFORTS, default='low')
    parser.add_argument('--max-output-tokens', type=int, default=4096)
    parser.add_argument('--dry-run', action='store_true', help='只展示请求，不联网、不收费')
    parser.add_argument('--output', type=Path, help='可选：保存完整 API JSON，可能含输入输出')
    args = parser.parse_args(argv)
    try:
        if not 1 <= args.max_output_tokens <= 128000:
            raise ValueError('--max-output-tokens 应为 1 至 128000。')
        if args.output and args.output.exists() and not args.dry_run:
            raise ValueError('输出文件已存在，请指定新路径避免覆盖。')
        payload = build_request(args)
        if args.dry_run:
            display = json.loads(json.dumps(payload))
            if args.mode == 'vision':
                display['input'][0]['content'][1]['image_url'] = '[本地图片的 base64 内容已省略]'
            print(json.dumps(display, ensure_ascii=False, indent=2))
            return 0
        key = os.environ.get('OPENAI_API_KEY', '').strip()
        if not key:
            raise ValueError('缺少 OPENAI_API_KEY，请设置环境变量或加 --dry-run。')
        response = call_api(payload, key)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with args.output.open('x', encoding='utf-8') as file:
                json.dump(response, file, ensure_ascii=False, indent=2)
        result, citations = read_output(response)
        if args.mode == 'extract':
            result = json.dumps(json.loads(result), ensure_ascii=False, indent=2)
        print(result)
        if citations:
            print('\n引用来源：')
            for title, url in citations:
                print(f'- {title}: {url}')
        if response.get('usage'):
            print('Token 用量：' + json.dumps(response['usage'], ensure_ascii=False), file=sys.stderr)
        return 0
    except urllib.error.HTTPError as exc:
        hints = {400: '检查参数和图片格式', 401: '检查 API key', 403: '检查项目与模型权限',
                 404: '检查模型访问权限', 429: '检查余额或限流，稍后再试'}
        print(f'API HTTP {exc.code}：{hints.get(exc.code, "服务异常，请稍后检查")}。', file=sys.stderr)
    except (ValueError, OSError, urllib.error.URLError) as exc:
        print(f'错误：{exc}', file=sys.stderr)
    return 1


if __name__ == '__main__':
    sys.exit(main())
