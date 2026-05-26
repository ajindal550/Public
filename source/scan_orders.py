"""Scan orders.md for unfenced JSON blocks and HTTP request lines."""
with open('/app/docs/orders.md') as f:
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

print("=== Candidate unfenced JSON/code blocks (>= 3 lines) ===")
for a, b in ranges:
    if b - a >= 2:
        first = lines[a - 1][:90]
        print(f"  Lines {a:4d}-{b:4d}  ({b-a+1:3d} lines)  | {first}")

print()
print("=== HTTP method lines outside code fences ===")
in_fence = False
for i, l in enumerate(lines, 1):
    s = l.strip()
    if s.startswith('```'):
        in_fence = not in_fence
        continue
    if in_fence:
        continue
    if s.startswith(('GET /', 'POST /', 'PUT /', 'DELETE /', 'PATCH /')) and len(s) < 200:
        print(f"  L{i:4d}: {s}")
