print("Topic: Exercise Mergeing the PDF FIle ")
import os
from PyPDF2 import PdfWriter,PdfReader


merge = PdfWriter()

file = os.listdir("/media/dark/USBNTFS/FinalProject/Python/Python")
print(file)

for i in file:
    reader = PdfReader(file)
    merge.add_page(reader.pages)

with open("/media/dark/USBNTFS/FinalProject/Python/Python/MergedFile.pdf","wb") as output:
    merge.write(output)