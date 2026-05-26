"""Wrap every unfenced JSON / HTTP-request block in orders.md with proper code fences.

Rules:
- Track ``` fences and never touch content inside them.
- A JSON block starts on a line whose stripped form starts with `{` or `[`
  (and the previous line is not already inside a fence). Continue collecting until
  brace/bracket depth returns to 0.
- An HTTP request block starts on a line whose stripped form starts with
  GET/POST/PUT/DELETE/PATCH followed by a space and `/...` path. Include any
  following Host:, Content-Type:, Authorization:, etc. lines and a possible
  blank-line + JSON body (the JSON body gets included so the request + body
  is one block).
"""
import re

SRC = '/app/docs/orders.md'

with open(SRC) as f:
    lines = f.read().split('\n')

out = []
i = 0
n = len(lines)
in_fence = False

http_method_re = re.compile(r'^(GET|POST|PUT|DELETE|PATCH)\s+/\S')

def is_header_line(s):
    return re.match(r'^[A-Z][A-Za-z\-]+:\s', s) is not None

while i < n:
    line = lines[i]
    stripped = line.strip()

    # Toggle fence state
    if stripped.startswith('```'):
        in_fence = not in_fence
        out.append(line)
        i += 1
        continue

    if in_fence:
        out.append(line)
        i += 1
        continue

    # Detect HTTP request block
    if http_method_re.match(stripped):
        block = [line]
        j = i + 1
        # Collect header lines
        while j < n:
            s = lines[j].strip()
            if is_header_line(s):
                block.append(lines[j])
                j += 1
            else:
                break
        # Optional blank line then JSON body
        body_start = None
        if j < n and lines[j].strip() == '':
            if j + 1 < n and lines[j + 1].strip().startswith(('{', '[')):
                block.append(lines[j])  # the blank
                body_start = j + 1
        if body_start is not None:
            # collect balanced JSON
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

    # Detect standalone JSON block
    if stripped.startswith('{') or stripped.startswith('['):
        # Only treat as block if length >= 3 lines balanced
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
# Collapse triple blank lines
new_text = re.sub(r'\n{3,}', '\n\n', new_text)

with open(SRC, 'w') as f:
    f.write(new_text)

print('Done. Total lines:', len(out))
