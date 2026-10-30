print("File Handling")

# File handling means creating, opening, reading, writing, and modifying files using Python.

# FileOpen = open("filename", "r")
# FileOpen.close()
# FileOpen.read()
# FileOpen.readline() // Read lines of the File
# FileOpen.write("Welcome to the class")

print("For reading a document:")

from docx import Document

print("File Handling")

file = Document(r"D:\download-folder d\📘 HUMAN VALUES AND ETHICS.docx")

for line in file.paragraphs:
    print(line.text)



print("For reading a pdf:")

from pypdf import PdfReader

print("File Handling")

file = PdfReader(r"D:\download-folder d\11.a oose.pdf")

for line in file.pages:
    print(line.extract_text())



# reading files using pandas library

# Reading files using Pandas library

import pandas as pd

df = pd.read_excel(r"D:\download-folder d\Petrol.xlsx")
print(df)
#print(df.head())       # First 5 rows
#print(df.tail())       # Last 5 rows
#print(df.shape)        # (121, 5)
#print(df.columns)      # Column names
#print(df.to_string())  # All rows and columns