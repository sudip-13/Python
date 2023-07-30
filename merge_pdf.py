import os
from pypdf import PdfWriter
pd=os.listdir("oscreation")
merger=PdfWriter()
for files in pd:
    if files.endswith(".pdf"):
        # print(files)
        merger.append(f"oscreation/{files}")
merger.write("merged-pdf.pdf")
merger.close()