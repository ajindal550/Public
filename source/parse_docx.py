"""Parse the Octopus Bridge docx into clean structured text by walking the document body
in order (paragraphs + tables) so we preserve flow."""
from docx import Document
from docx.oxml.ns import qn

doc = Document("/app/source/octopus.docx")

def iter_block_items(parent):
    body = parent.element.body
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            # paragraph
            from docx.text.paragraph import Paragraph
            yield ("p", Paragraph(child, parent))
        elif child.tag == qn("w:tbl"):
            from docx.table import Table
            yield ("t", Table(child, parent))

out = []
for kind, item in iter_block_items(doc):
    if kind == "p":
        text = item.text.strip()
        style = item.style.name if item.style else ""
        if text:
            if "Heading" in style:
                level = "".join(c for c in style if c.isdigit()) or "1"
                out.append(f"\n{'#'*int(level)} {text}\n")
            else:
                out.append(text)
        else:
            out.append("")
    else:
        # table
        out.append("\n[TABLE]")
        for row in item.rows:
            cells = [c.text.strip().replace("\n", " ") for c in row.cells]
            out.append("| " + " | ".join(cells) + " |")
        out.append("[/TABLE]\n")

with open("/app/source/octopus_raw.md", "w") as f:
    f.write("\n".join(out))

print("Wrote", len("\n".join(out)), "chars")
print("Lines:", len(out))
