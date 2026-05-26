"""Generic fence-wrapping scanner+fixer for any docs/*.md file.

Detects:
- Unfenced JSON blocks (balanced { } or [ ] of >= 3 lines).
- Unfenced HTTP request lines (GET/POST/PUT/DELETE/PATCH) + headers + optional body.
- Lines whose stripped form is a single `{`, `}`, `[`, `]` (continuation of a JSON
  block whose start was missed).

Wraps them in ```json or ```http fences. Skips content already inside fences.
"""
import re
import sys

http_method_re = re.compile(r'^(GET|POST|PUT|DELETE|PATCH)\s+/\S')

def is_header_line(s):
    return re.match(r'^[A-Z][A-Za-z\-]+:\s', s) is not None

def fix_file(path):
    with open(path) as f:
        lines = f.read().split('\n')

    out = []
    i = 0
    n = len(lines)
    in_fence = False

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith('```'):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue

        if in_fence:
            out.append(line)
            i += 1
            continue

        # HTTP request block
        if http_method_re.match(stripped):
            block = [line]
            j = i + 1
            while j < n and is_header_line(lines[j].strip()):
                block.append(lines[j])
                j += 1
            # optional body
            body_start = None
            if j < n and lines[j].strip() == '':
                if j + 1 < n and lines[j + 1].strip().startswith(('{', '[')):
                    block.append(lines[j])
                    body_start = j + 1
            if body_start is not None:
                depth = 0
                k = body_start
                while k < n:
                    s = lines[k]
                    block.append(s)
                    depth += s.count('{') - s.count('}') + s.count('[') - s.count(']')
                    k += 1
                    if depth <= 0 and lines[k - 1].strip() and any(c in lines[k - 1] for c in '}]'):
                        break
                j = k
            out.append('```http')
            out.extend(block)
            out.append('```')
            i = j
            continue

        # JSON block
        if stripped.startswith('{') or stripped.startswith('['):
            depth = stripped.count('{') - stripped.count('}') + stripped.count('[') - stripped.count(']')
            if depth > 0:
                block = [line]
                j = i + 1
                while j < n and depth > 0:
                    s = lines[j]
                    block.append(s)
                    depth += s.count('{') - s.count('}') + s.count('[') - s.count(']')
                    j += 1
                if len(block) >= 3:
                    out.append('```json')
                    out.extend(block)
                    out.append('```')
                    i = j
                    continue

        out.append(line)
        i += 1

    new_text = '\n'.join(out)
    new_text = re.sub(r'\n{3,}', '\n\n', new_text)
    with open(path, 'w') as f:
        f.write(new_text)
    return len(out)


def scan_file(path):
    with open(path) as f:
        lines = f.read().split('\n')
    in_fence = False
    ranges = []
    start = None
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if s.startswith('```'):
            in_fence = not in_fence
            if start:
                ranges.append((start, i - 1))
                start = None
            continue
        if in_fence:
            if start:
                ranges.append((start, i - 1))
                start = None
            continue
        is_json_like = s and (s[0] in '{["}],' or s.startswith('"'))
        if is_json_like and start is None:
            start = i
        elif (not is_json_like) and start is not None and s != '':
            ranges.append((start, i - 1))
            start = None
    if start:
        ranges.append((start, len(lines)))

    blocks = []
    for a, b in ranges:
        if b - a >= 2:
            first = lines[a - 1][:90]
            blocks.append(f"  L{a:4d}-{b:4d} ({b-a+1:3d}L)  | {first}")

    http_lines = []
    in_fence = False
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if s.startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if http_method_re.match(s) and len(s) < 200:
            http_lines.append(f"  L{i:4d}: {s}")

    return blocks, http_lines


if __name__ == '__main__':
    files = sys.argv[1:] or ['purchase-orders.md', 'customers.md', 'transactions.md']
    for fn in files:
        path = f'/app/docs/{fn}'
        print(f'\n=========== {fn} BEFORE ===========')
        blocks, http_lines = scan_file(path)
        if blocks:
            print('Unfenced JSON/code blocks:')
            for b in blocks:
                print(b)
        if http_lines:
            print('Unfenced HTTP lines:')
            for h in http_lines:
                print(h)
        if not blocks and not http_lines:
            print('  (clean)')

        fix_file(path)

        print(f'=========== {fn} AFTER ===========')
        blocks, http_lines = scan_file(path)
        if blocks:
            print('Unfenced JSON/code blocks (REMAINING):')
            for b in blocks:
                print(b)
        if http_lines:
            print('Unfenced HTTP lines (REMAINING):')
            for h in http_lines:
                print(h)
        if not blocks and not http_lines:
            print('  ✅ clean')
