#!/usr/bin/env python3
from pypdf import PdfReader

reader = PdfReader("tests_exam.pdf")
number_of_pages = len(reader.pages)
page1 = reader.pages[0]
page2 = reader.pages[1]
text1 = page1.extract_text()
text2 = page2.extract_text()
print(text1)
print(text2)

