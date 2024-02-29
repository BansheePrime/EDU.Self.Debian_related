#!/usr/bin/env python3
from pathlib import Path
from pypdf import PdfReader

pdf_path = (
    Path.home()
    / "Public"
    / "EDU.Self.Debian_related"
    / "pdf_parsing"
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "Pride_and_Prejudice.pdf"
)

pdf_reader = Pdfreader(pdf_path)
txt_file = Path.home() / "Pride_and_Prejudice.txt"
content = [
    f"{pdf_reader.metadata.title}",
    f"Number of pages: {len(pdf_reader.pages)}"
]

for page in pdf_reader.pages:
    content.append(page.extract_text())

txt_file.write_text("\n".join(content))

