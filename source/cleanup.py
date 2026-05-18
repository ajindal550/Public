"""Clean up the raw markdown and split into per-section files.

- Convert [TABLE]...[/TABLE] markers into proper GFM tables (with --- separator).
- Detect JSON code blocks (consecutive lines starting with { / "field": / } / [ / ])
  and wrap them in ```json fences.
- Detect curl blocks and wrap in ```bash.
- Normalize typographic quotes.
- Split into per top-level section files.
"""
import re
import os
import json

SRC = "/app/source/octopus_raw.md"
OUT_DIR = "/app/octopus-bridge-docs/docs"
os.makedirs(OUT_DIR, exist_ok=True)

with open(SRC) as f:
    raw = f.read()

# 1. Normalize typographic quotes
raw = (raw
       .replace("\u201c", '"').replace("\u201d", '"')
       .replace("\u2018", "'").replace("\u2019", "'")
       .replace("\u2013", "-").replace("\u2014", "-")
       .replace("\u00a0", " "))

# 2. Convert tables
def convert_tables(text):
    out = []
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "[TABLE]":
            # collect rows until [/TABLE]
            i += 1
            rows = []
            while i < len(lines) and lines[i].strip() != "[/TABLE]":
                if lines[i].strip().startswith("|"):
                    rows.append(lines[i])
                i += 1
            i += 1  # skip [/TABLE]
            if rows:
                out.append("")
                out.append(rows[0])
                # add separator based on first row col count
                ncols = rows[0].count("|") - 1
                if ncols > 0:
                    out.append("|" + " --- |" * ncols)
                out.extend(rows[1:])
                out.append("")
        else:
            out.append(line)
            i += 1
    return "\n".join(out)

raw = convert_tables(raw)

# 3. Detect & wrap JSON / curl blocks
def wrap_code_blocks(text):
    lines = text.split("\n")
    out = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        # curl block detection
        if stripped.startswith("curl ") or stripped.startswith("curl-"):
            block = [line]
            j = i + 1
            # continuation lines (end with backslash) or follow-up flags
            while j < n:
                s = lines[j].rstrip()
                if not s:
                    # one blank inside curl OK only if previous ended with \
                    break
                if (block[-1].rstrip().endswith("\\")
                        or s.lstrip().startswith("--")
                        or s.lstrip().startswith("-H")
                        or s.lstrip().startswith("-d")
                        or s.lstrip().startswith("-X")
                        or s.lstrip().startswith("'")):
                    block.append(lines[j])
                    j += 1
                else:
                    break
            out.append("```bash")
            out.extend(block)
            out.append("```")
            i = j
            continue

        # JSON block detection: starts with { or [ on its own line
        if stripped in ("{", "[") or (stripped.startswith("{") and not stripped.endswith("}")):
            # find balanced end
            block = [line]
            depth = stripped.count("{") - stripped.count("}") + stripped.count("[") - stripped.count("]")
            j = i + 1
            while j < n and depth > 0:
                block.append(lines[j])
                s = lines[j]
                # naive depth counting ignoring strings—works well here
                depth += s.count("{") - s.count("}") + s.count("[") - s.count("]")
                j += 1
            # block must be at least 3 lines to qualify
            if len(block) >= 3:
                out.append("```json")
                out.extend(block)
                out.append("```")
                i = j
                continue

        out.append(line)
        i += 1
    return "\n".join(out)

raw = wrap_code_blocks(raw)

# 4. Split into top-level sections
# Pattern: ^# N. Title
section_re = re.compile(r"^# (\d+)\. (.+)$", re.MULTILINE)
matches = list(section_re.finditer(raw))

# Build intro (everything before first section)
intro_end = matches[0].start() if matches else len(raw)
intro = raw[:intro_end].strip()

# Build sections
SECTIONS = {
    1: ("authentication", "Authentication"),
    2: ("shop", "Shop"),
    3: ("products", "Products"),
    4: ("images", "Images"),
    5: ("variants", "Variants"),
    6: ("locations", "Locations"),
    7: ("inventory", "Inventory Levels"),
    8: ("collections", "Custom Collections"),
    9: ("collects", "Collects"),
    10: ("orders", "Orders"),
    11: ("purchase-orders", "Purchase Orders"),
    12: ("customers", "Customers"),
    13: ("transactions", "Transactions"),
    14: ("faq", "FAQ"),
    15: ("mapping", "Mapping Considerations"),
    16: ("samples", "Sample Code"),
}

# Some duplicate `# N.` headings inside Orders confuse splitting. Keep only those
# whose number appears for the FIRST time in document order.
seen = set()
clean_matches = []
for m in matches:
    num = int(m.group(1))
    if num in SECTIONS and num not in seen:
        seen.add(num)
        clean_matches.append(m)

for idx, m in enumerate(clean_matches):
    num = int(m.group(1))
    slug, title = SECTIONS[num]
    start = m.start()
    end = clean_matches[idx + 1].start() if idx + 1 < len(clean_matches) else len(raw)
    body = raw[start:end].strip()
    # Replace top heading
    body = re.sub(r"^# \d+\. .+$", f"# {title}", body, count=1, flags=re.MULTILINE)
    # Collapse 3+ blank lines
    body = re.sub(r"\n{3,}", "\n\n", body)
    with open(os.path.join(OUT_DIR, f"{slug}.md"), "w") as f:
        f.write(body + "\n")
    print(f"Wrote docs/{slug}.md  ({len(body)} chars)")

# Write intro as index
with open(os.path.join(OUT_DIR, "intro_extracted.md"), "w") as f:
    f.write(intro + "\n")

print("\nDone.")
