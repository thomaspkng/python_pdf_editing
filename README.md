# python_pdf_editing (Python PDF Editing)

This is a python script using TKinter and PyPDF2 to create an application to merge some (up to 10 files right now) PDF files into one PDF file and Extract some page(s) from a PDF.

## Features

Simple PDF files Merging and Extracting page(s) from PDF file is the essential functions of this script.

__MERGE PDF__

By using PyPDF2, reading pdf(s) into list and combined into one sigle PDF file.

__Extract PDF__

By reading the number of pages of the selecteed PDF file, one (1) range of page(s) can be select for extracted from the file and save as separated PDF file.


### Convert to EXE file

The .exe file is converted from .py file with PyInstaller:

>&gt;pyinstaller --onefile -- windowed pdf_editing.py


(TN-20220718)
___
