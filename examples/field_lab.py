#!/usr/bin/env python3
"""Original, offline teaching lab: verified calculations -> JSON + SVG reports.

No network, model calls, external images, fonts, or packages are required.
The SVG drawing code and fictional fixture were created for this repository.
"""
import argparse
from html import escape
import json
from pathlib import Path
import sys

DEFAULT_BRIEF = Path(__file__).with_name('fixtures') / 'studio-brief.json'


def integer(value, name, minimum=0, maximum=1000000):
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(f'{name}: expected an integer in [{minimum}, {maximum}]')
    return value


def label(value, name, maximum=50):
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise ValueError(f'{name}: expected 1–{maximum} characters')
    return value


def evaluate_brief(brief, *, budget=None, guests=None):
    """Calculate verifiable results. Never interpret these as model predictions."""
    label(brief['title'], 'title', 36)
    workshop, film, release = (brief[key] for key in ('workshop', 'film', 'release'))
    if workshop['currency'] != 'CNY':
        raise ValueError('This exercise uses CNY; no currency conversion is performed.')
    budget = integer(workshop['budget'] if budget is None else budget, 'budget', 1)
    guests = integer(workshop['guests'] if guests is None else guests, 'guests', 1, 200)
    reserve = integer(workshop['reserve_percent'], 'reserve_percent', 0, 100)
    costs = workshop['costs']
    if not isinstance(costs, list) or not 1 <= len(costs) <= 5:
        raise ValueError('Provide 1–5 cost lines for this report.')
    items = []
    for item in costs:
        label(item['label'], 'cost label', 30)
        unit = integer(item['unit_cost'], 'unit_cost')
        if item['basis'] not in ('fixed', 'guest'):
            raise ValueError('Cost basis must be fixed or guest.')
        quantity = guests if item['basis'] == 'guest' else 1
        items.append(dict(label=item['label'], unit_cost=unit, quantity=quantity, total=quantity * unit))
    total = sum(item['total'] for item in items)
    remainder = budget - total
    # Compare integer products, avoiding rounding the reserve threshold.
    reserve_met = remainder * 100 >= budget * reserve
    fps = integer(film['fps'], 'fps', 1, 120)
    target = integer(film['target_seconds'], 'target_seconds', 1, 600)
    if not isinstance(film['shots'], list) or len(film['shots']) != 3:
        raise ValueError('This storyboard exercise requires exactly three shots.')
    shots, cursor, shot_ids = [], 0, set()
    for shot in film['shots']:
        name = label(shot['id'], 'shot id', 8)
        if name in shot_ids:
            raise ValueError('Shot IDs must be unique.')
        shot_ids.add(name)
        label(shot['title'], 'shot title', 18)
        label(shot['caption'], 'shot caption', 44)
        seconds = integer(shot['seconds'], 'shot seconds', 1, 200)
        frames = seconds * fps
        shots.append(dict(shot, start_frame=cursor, end_frame_exclusive=cursor + frames))
        cursor += frames
    checks = release['checks']
    if not isinstance(checks, list) or not 1 <= len(checks) <= 5:
        raise ValueError('Provide 1–5 release checks for this report.')
    results, check_ids = [], set()
    for check in checks:
        check_id = label(check['id'], 'check id', 8)
        if check_id in check_ids:
            raise ValueError('Check IDs must be unique.')
        check_ids.add(check_id)
        label(check['label'], 'check label', 36)
        label(check['owner'], 'owner', 16)
        for key in ('expected', 'observed'):
            value = check[key]
            if type(value) not in (bool, int):
                raise ValueError('Check values must be booleans or integers.')
            if type(value) is int:
                integer(value, key)
        passed = type(check['observed']) is type(check['expected']) and check['observed'] == check['expected']
        results.append(dict(check, passed=passed))
    return {
        'title': brief['title'],
        'mode': 'offline_fixture',
        'workshop': dict(currency='CNY', budget=budget, guests=guests, items=items,
                         spent=total, remainder=remainder, reserve_percent=reserve,
                         reserve_met=reserve_met, within_budget=remainder >= 0),
        'film': dict(fps=fps, target_seconds=target, shots=shots, total_frames=cursor,
                     duration_matches=cursor == target * fps),
        'release': dict(checks=results, passed=sum(c['passed'] for c in results),
                        total=len(results), ready=all(c['passed'] for c in results)),
    }


class Canvas:
    """Small SVG writer; all text is XML-escaped and all drawings are local."""
    def __init__(self, title, background, ink):
        self.ink = ink
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720" role="img" aria-label="{escape(title, quote=True)}">',
                      f'<title>{escape(title)}</title>',
                      '<desc>Original flaq.ai teaching report. Offline calculations using fictional data; not an API response or third-party product.</desc>',
                      '<style>text{font-family:Arial,Helvetica,sans-serif} .mono{font-family:monospace}</style>']
        self.rect(0, 0, 1280, 720, background)

    def rect(self, x, y, w, h, fill, radius=0, stroke='none'):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')

    def text(self, x, y, value, size=18, color=None, weight=400, anchor='start'):
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color or self.ink}" font-weight="{weight}" text-anchor="{anchor}">{escape(str(value))}</text>')

    def line(self, x1, y1, x2, y2, color, width=1):
        self.parts.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" stroke-width="{width}" fill="none"/>')

    def circle(self, x, y, radius, fill, stroke='none'):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="{stroke}"/>')

    def end(self):
        return '\n'.join(self.parts + ['</svg>']) + '\n'


def header(c, number, title, subtitle, muted):
    c.text(48, 43, 'flaq.ai  /  ASTRA FIELD LAB', 15, weight=700)
    c.text(1232, 43, f'EXPERIMENT {number}   ·   OFFLINE / FICTIONAL DATA', 13, muted, anchor='end')
    c.text(48, 112, title, 48, weight=700)
    c.text(48, 146, subtitle, 18, muted)


def footer(c, command, muted):
    c.line(48, 668, 1232, 668, muted)
    c.text(48, 694, command, 13, muted)
    c.text(1232, 694, 'Original code + fixture + reproducible report', 13, muted, anchor='end')


def render_budget(data):
    w = data['workshop']
    c = Canvas('Workshop budget report', '#F4F0E7', '#222820')
    header(c, '01', 'Make the numbers work.', data['title'] + '  /  A workshop budget with a checkable reserve.', '#667160')
    metrics = [('BUDGET / CNY', f"{w['budget']:,}"), ('PLANNED SPEND', f"{w['spent']:,}"), ('RESERVE / CNY', f"{w['remainder']:,}")]
    for i, (name, value) in enumerate(metrics):
        x = 48 + i * 400
        c.rect(x, 184, 384, 126, '#D9E7BF' if i == 2 else '#FFFDF8', 16)
        c.text(x + 24, 216, name, 13, '#65705F', 700)
        c.text(x + 24, 278, value, 48, weight=700)
    c.rect(48, 334, 760, 300, '#FFFDF8', 16)
    c.text(72, 370, 'WHAT THE WORKSHOP NEEDS', 13, '#667160', 700)
    for i, row in enumerate(w['items']):
        y = 412 + i * 45
        c.text(72, y, row['label'], 19)
        c.text(420, y, f"{row['quantity']} × {row['unit_cost']}", 16, '#667160')
        c.text(780, y, f"CNY {row['total']:,}", 20, weight=700, anchor='end')
        if i < 4: c.line(72, y + 15, 780, y + 15, '#E9E5DA')
    c.rect(832, 334, 400, 300, '#26362D', 16)
    c.text(860, 373, 'ROOM TO ADJUST', 13, '#C6D8AD', 700)
    c.text(860, 432, f"{w['guests']} guests", 38, '#F9F9ED', 700)
    ratio = min(1, max(0, w['spent'] / w['budget']))
    c.rect(860, 463, 344, 12, '#6C7867', 6)
    c.rect(860, 463, round(344 * ratio), 12, '#C2E080', 6)
    c.text(860, 512, f"Reserve target: {w['reserve_percent']}%", 20, '#F9F9ED')
    c.text(860, 554, 'TARGET MET' if w['reserve_met'] else 'REPLAN REQUIRED', 25, '#C2E080' if w['reserve_met'] else '#FFC29C', 700)
    c.text(860, 594, 'Change guests or budget, then rerun.', 17, '#C6D8AD')
    footer(c, 'python3 examples/field_lab.py --budget 2600 --guests 24', '#667160')
    return c.end()


def render_storyboard(data):
    f = data['film']
    c = Canvas('Paper circuit storyboard', '#171C2B', '#F6F3EB')
    header(c, '02', 'A small story. Every frame counted.', f"{f['target_seconds']} seconds  /  {f['fps']} fps  /  Original procedural vector artwork", '#A8B4CB')
    colors = ['#F0B786', '#A4C9C7', '#C3BAE5']
    for i, shot in enumerate(f['shots']):
        x = 48 + i * 400
        c.rect(x, 188, 384, 370, '#252D40', 18)
        c.rect(x + 16, 204, 352, 194, colors[i], 12)
        # Three original paper-circuit compositions, made only from primitives.
        c.rect(x + 96, 226, 190, 144, '#F8F3E8', 6)
        for j in range(3): c.line(x + 117, 250 + j * 18, x + 180, 250 + j * 18, '#A8A695', 3)
        c.line(x + 142, 326, x + 252, 326, '#D47C42', 7)
        c.line(x + 252, 326, x + 252, 264, '#D47C42', 7)
        c.circle(x + 252, 264, 15 + i * 4, '#FFF1A6' if i > 0 else '#CEC9BC', '#635C4D')
        c.circle(x + 142, 326, 14, '#343E50')
        if i == 2:
            for dx, dy in [(-30, -25), (30, -25), (0, -39)]:
                c.line(x + 252 + dx, 264 + dy, x + 252 + dx * 1.25, 264 + dy * 1.25, '#866634', 3)
        c.text(x + 24, 434, shot['id'] + ' / ' + shot['title'], 25, weight=700)
        c.text(x + 24, 472, shot['caption'], 15, '#BFCADE')
        c.text(x + 24, 522, f"{shot['seconds']}s   ·   frames [{shot['start_frame']}, {shot['end_frame_exclusive']})", 18, '#D1E6E3')
    total = f['total_frames']
    x = 48
    for i, shot in enumerate(f['shots']):
        width = (shot['end_frame_exclusive'] - shot['start_frame']) / total * 1184
        c.rect(round(x), 586, round(width) - 3, 18, colors[i], 4)
        x += width
    state = 'DURATION MATCHES' if f['duration_matches'] else 'DURATION MISMATCH'
    c.text(48, 640, f"{total} frames  /  {state}", 19, '#D1E6E3', 700)
    c.text(1232, 640, 'Intervals are start-inclusive, end-exclusive.', 16, '#A8B4CB', anchor='end')
    footer(c, 'python3 examples/field_lab.py', '#A8B4CB')
    return c.end()


def render_release(data):
    r = data['release']
    c = Canvas('Release acceptance report', '#EAF0F9', '#172C4A')
    header(c, '03', 'Show the evidence before release.', data['title'] + '  /  Simulated observations, checked by explicit rules.', '#60738F')
    c.rect(48, 186, 328, 448, '#193855', 18)
    c.text(78, 228, 'RELEASE DECISION', 14, '#AAC1D9', 700)
    c.text(78, 302, 'READY' if r['ready'] else 'HOLD', 64, '#B3E2D0' if r['ready'] else '#FFD19F', 700)
    c.text(78, 352, f"{r['passed']} / {r['total']} checks passed", 24, '#F1F5FA')
    c.line(78, 386, 346, 386, '#53728B')
    c.text(78, 428, 'Treat a missing requirement', 18, '#CDDBEA')
    c.text(78, 457, 'as a task to resolve.', 18, '#CDDBEA')
    c.text(78, 514, 'No inferred passes.', 22, '#B3E2D0', 700)
    c.text(78, 584, 'Source: studio-brief.json', 15, '#AAC1D9')
    c.rect(400, 186, 832, 448, '#FFFFFF', 18)
    c.text(426, 224, 'ACCEPTANCE CHECK', 13, '#60738F', 700)
    c.text(900, 224, 'ACTUAL / TARGET', 13, '#60738F', 700, 'middle')
    c.text(1160, 224, 'RESULT', 13, '#60738F', 700, 'middle')
    show = lambda v: str(v).lower() if isinstance(v, bool) else str(v)
    for i, check in enumerate(r['checks']):
        y = 271 + i * 72
        c.text(426, y, check['label'], 19, weight=700)
        c.text(426, y + 23, check['id'] + '  /  ' + check['owner'], 14, '#60738F')
        c.text(900, y + 10, f"{show(check['observed'])} / {show(check['expected'])}", 18, anchor='middle')
        c.rect(1104, y - 14, 112, 36, '#E0F2E9' if check['passed'] else '#FFE5D6', 18)
        c.text(1160, y + 10, 'PASS' if check['passed'] else 'FIX', 15, '#245E4A' if check['passed'] else '#924B27', 700, 'middle')
        if i < len(r['checks']) - 1: c.line(426, y + 40, 1206, y + 40, '#E8EEF5')
    footer(c, 'python3 examples/field_lab.py  /  deterministic comparison of fixture values', '#60738F')
    return c.end()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--brief', type=Path, default=DEFAULT_BRIEF)
    parser.add_argument('--budget', type=int)
    parser.add_argument('--guests', type=int)
    parser.add_argument('--out', type=Path, default=Path('outputs/field-lab'))
    parser.add_argument('--overwrite', action='store_true', help='Replace previously generated files in the output directory.')
    args = parser.parse_args(argv)
    try:
        if args.brief.stat().st_size > 65536:
            raise ValueError('Brief must be at most 64 KiB.')
        brief = json.loads(args.brief.read_text(encoding='utf-8'))
        result = evaluate_brief(brief, budget=args.budget, guests=args.guests)
        files = {'workshop-budget.svg': render_budget(result), 'craft-storyboard.svg': render_storyboard(result),
                 'release-review.svg': render_release(result), 'results.json': json.dumps(result, ensure_ascii=False, indent=2) + '\n'}
        if not args.overwrite and any((args.out / name).exists() for name in files):
            raise ValueError('Output exists. Use a new --out directory or --overwrite.')
        args.out.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            (args.out / name).write_text(content, encoding='utf-8')
        print(json.dumps({'directory': str(args.out), 'files': list(files), 'mode': result['mode'],
                          'spent': result['workshop']['spent'], 'frames': result['film']['total_frames'],
                          'release_ready': result['release']['ready']}, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'Invalid brief or output: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
