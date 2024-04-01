import pypdf
import sys
import os

merger = pypdf.PdfWriter()

for pdf in [r"\Users\MEMEMEMEME2\Documents\python_projects\pdf_merger\pdf_original\1.pdf", r"\Users\MEMEMEMEME2\Documents\python_projects\pdf_merger\pdf_original\2.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()