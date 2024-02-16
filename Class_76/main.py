from PyPDF2 import PdfWriter, PdfReader

import os

merger = PdfWriter()

files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    with open(pdf, "rb") as file:
        reader = PdfReader(file)
        merger.add_pages(reader.pages)

with open("Merged-pdf.pdf", "wb") as output_file:
    merger.write(output_file)
