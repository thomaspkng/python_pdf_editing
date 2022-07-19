# First Issue, verion: 0.1.227191
import os
from os.path import isdir, isfile, join
import time
from datetime import datetime
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import font as tkf

# define functions
## functions for PDF_MERGE
### Open file for merge
def openfilepath_merge(fno_merge):
	file2merge = filedialog.askopenfilename(title='PDF(s) for merge', filetypes=(('PDF files', '*.pdf'),('ALL FILES', '*.*')))
	if file2merge != "":
		# set the output folder to current file location
		folder_now_merge = os.path.dirname(file2merge)
		outFolder_entry_merge.delete(0,END)
		outFolder_entry_merge.insert(0,folder_now_merge)
		# for each entry update file data
		match fno_merge:
			case 1:
				fileMerge_entry_1.configure(state="normal")
				fileMerge_entry_1.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_1.insert(0,str(file2merge)) # add the file location to fileopen_location_entry
				fileMerge_entry_1.configure(state="readonly")
				mergeNot_1.set(1)
			case 2:
				fileMerge_entry_2.configure(state="normal")
				fileMerge_entry_2.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_2.insert(0,str(file2merge)) # add the file location to fileopen_location_entry
				fileMerge_entry_2.configure(state="readonly")
				mergeNot_2.set(1)
			case 3:
				fileMerge_entry_3.configure(state="normal")
				fileMerge_entry_3.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_3.insert(0,str(file2merge)) # add the file location to fileopen_location_entry
				fileMerge_entry_3.configure(state="readonly")
				mergeNot_3.set(1)
			case 4:
				fileMerge_entry_4.configure(state="normal")
				fileMerge_entry_4.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_4.insert(0,str(file2merge)) # add the file location to fileopen_location_entry
				fileMerge_entry_4.configure(state="readonly")
				mergeNot_4.set(1)
			case 5:
				fileMerge_entry_5.configure(state="normal")
				fileMerge_entry_5.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_5.insert(0,str(file2merge)) # add the file location to fileopen_location_entry
				fileMerge_entry_5.configure(state="readonly")
				mergeNot_5.set(1)
			case 6:
				fileMerge_entry_6.configure(state="normal")
				fileMerge_entry_6.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_6.insert(0,str(file2merge)) # add the file location to fileopen_location_entry
				fileMerge_entry_6.configure(state="readonly")
				mergeNot_6.set(1)
			case 7:
				fileMerge_entry_7.configure(state="normal")
				fileMerge_entry_7.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_7.insert(0,str(file2merge)) # add the file location to fileopen_location_entry
				fileMerge_entry_7.configure(state="readonly")
				mergeNot_7.set(1)
			case 8:
				fileMerge_entry_8.configure(state="normal")
				fileMerge_entry_8.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_8.insert(0,str(file2merge)) # add the file location to fileopen_location_entry
				fileMerge_entry_8.configure(state="readonly")
				mergeNot_8.set(1)
			case 9:
				fileMerge_entry_9.configure(state="normal")
				fileMerge_entry_9.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_9.insert(0,str(file2merge)) # add the file location to fileopen_location_entry
				fileMerge_entry_9.configure(state="readonly")
				mergeNot_9.set(1)
			case 10:
				fileMerge_entry_10.configure(state="normal")
				fileMerge_entry_10.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_10.insert(0,str(file2merge)) # add the file location to fileopen_location_entry
				fileMerge_entry_10.configure(state="readonly")
				mergeNot_10.set(1)

	if file2merge == "":
		match fno_merge:
			case 1:
				fileMerge_entry_1.configure(state="normal")
				fileMerge_entry_1.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_1.configure(state="readonly")
				mergeNot_1.set(0)
			case 2:
				fileMerge_entry_2.configure(state="normal")
				fileMerge_entry_2.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_2.configure(state="readonly")
				mergeNot_2.set(0)
			case 3:
				fileMerge_entry_3.configure(state="normal")
				fileMerge_entry_3.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_3.configure(state="readonly")
				mergeNot_3.set(0)
			case 4:
				fileMerge_entry_4.configure(state="normal")
				fileMerge_entry_4.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_4.configure(state="readonly")
				mergeNot_4.set(0)
			case 5:
				fileMerge_entry_5.configure(state="normal")
				fileMerge_entry_5.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_5.configure(state="readonly")
				mergeNot_5.set(0)
			case 6:
				fileMerge_entry_6.configure(state="normal")
				fileMerge_entry_6.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_6.configure(state="readonly")
				mergeNot_6.set(0)
			case 7:
				fileMerge_entry_7.configure(state="normal")
				fileMerge_entry_7.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_7.configure(state="readonly")
				mergeNot_7.set(0)
			case 8:
				fileMerge_entry_8.configure(state="normal")
				fileMerge_entry_8.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_8.configure(state="readonly")
				mergeNot_8.set(0)
			case 9:
				fileMerge_entry_9.configure(state="normal")
				fileMerge_entry_9.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_9.configure(state="readonly")
				mergeNot_9.set(0)
			case 10:
				fileMerge_entry_10.configure(state="normal")
				fileMerge_entry_10.delete(0,END) # delete all content at Entry:fileopen_location_entry
				fileMerge_entry_10.configure(state="readonly")
				mergeNot_10.set(0)

### Open OUTPUT FOLDER
def outFolderLoc_merge():
	output_folder_merge = filedialog.askdirectory(title='OUTPUT LOCATION')
	if output_folder_merge != "":
		outFolder_entry_merge.delete(0,END)
		outFolder_entry_merge.insert(0,output_folder_merge)

### Merge PDFs
def mergePDF():
	merge_instance = PdfFileMerger()
	if mergeNot_1.get() != 0:
		if fileMerge_entry_1.get() != "":
			merge_instance.append(open(fileMerge_entry_1.get(),'rb'))
	if mergeNot_2.get() != 0:
		if fileMerge_entry_2.get() != "":
			merge_instance.append(open(fileMerge_entry_2.get(),'rb'))
	if mergeNot_3.get() != 0:
		if fileMerge_entry_3.get() != "":
			merge_instance.append(open(fileMerge_entry_3.get(),'rb'))
	if mergeNot_4.get() != 0:
		if fileMerge_entry_4.get() != "":
			merge_instance.append(open(fileMerge_entry_4.get(),'rb'))
	if mergeNot_5.get() != 0:
		if fileMerge_entry_5.get() != "":
			merge_instance.append(open(fileMerge_entry_5.get(),'rb'))
	if mergeNot_6.get() != 0:
		if fileMerge_entry_6.get() != "":
			merge_instance.append(open(fileMerge_entry_6.get(),'rb'))
	if mergeNot_7.get() != 0:
		if fileMerge_entry_7.get() != "":
			merge_instance.append(open(fileMerge_entry_7.get(),'rb'))
	if mergeNot_8.get() != 0:
		if fileMerge_entry_8.get() != "":
			merge_instance.append(open(fileMerge_entry_8.get(),'rb'))
	if mergeNot_9.get() != 0:
		if fileMerge_entry_9.get() != "":
			merge_instance.append(open(fileMerge_entry_9.get(),'rb'))
	if mergeNot_10.get() != 0:
		if fileMerge_entry_10.get() != "":
			merge_instance.append(open(fileMerge_entry_10.get(),'rb'))

	output_dir = outFolder_entry_merge.get()
	output_filename_merge = outfilename_entry_merge.get()
	if output_filename_merge == "":
		output_filename_merge = datetime.now().strftime('%Y%m%d-%H%M%S')

	if output_dir != "":
		filename_full_merge = output_dir + "/" + output_filename_merge + '.pdf'
	else:
		filename_full_merge = output_filename_merge + '.pdf'
	#print(filename_full_merge)
	#merge_instance.output(filename_full_merge, 'F')
	with open(filename_full_merge, "wb") as fileout_merge:
		merge_instance.write(fileout_merge)

## functions for PDF_EXTRACT
### open file
def openfilepath_extract():
	global file2extract # create a global variable
	file2extract = filedialog.askopenfilename(title='PDF for extract', filetypes=(('PDF files', '*.pdf'),('ALL FILES', '*.*')))
	if file2extract != "":
		fileopen_location_entry.configure(state="normal")
		fileopen_location_entry.delete(0,END) # delete all content at Entry:fileopen_location_entry
		fileopen_location_entry.insert(0,str(file2extract)) # add the file location to fileopen_location_entry
		fileopen_location_entry.configure(state="readonly")
		pdfGetTotalPage()

### get the total page after open the PDF file and refresh the page number for FROM and TO
def pdfGetTotalPage():
	global pdfReader
	pdf_path = fileopen_location_entry.get()
	pdfReader = PdfFileReader(pdf_path)
	pdf_pages_no = pdfReader.getNumPages()
	totalPage_entry.configure(state="normal")
	totalPage_entry.delete(0,END)
	totalPage_entry.insert(0,pdf_pages_no)
	totalPage_entry.configure(state="readonly")
	# list for show all page number
	newPageNoList = [x for x in range(1, pdf_pages_no+1)]
	# change page seletion for pagefr
	pagefr_menu['menu'].delete(0,END)
	for newPage in range(1, pdf_pages_no+1):
		#pagefr_menu['menu'].add_command(label=newPage, command=lambda x=newPage: pagefr_e.set(newPage))
		pagefr_menu['menu'].add_command(label=newPage, command=lambda x=newPage: pagefr_e.set(x))
	pagefr_e.set(newPageNoList[0])
	# change page seletion for pageto
	pageto_menu['menu'].delete(0,END)
	for newPage in range(1, pdf_pages_no+1):
		#pageto_menu['menu'].add_command(label=newPage, command=lambda x=newPage: pageto_e.set(newPage))
		#pageto_menu['menu'].add_command(label=newPage, command = tk._setit(pageto_e, newPage))
		pageto_menu['menu'].add_command(label=newPage, command=lambda x=newPage: pageto_e.set(x))
	pageto_e.set(newPageNoList[-1])

### when pagefr change, check if pagefr is larger than pageto
def pagefrchange(*evt): # will pass 3 parameters to function, use *evt to store for avoid error
	if int(totalPage_entry.get()) < 2: # if total page < 2, no need to do anything
		return
	#print(pagefr_e.get())
	# if fr > to, then to = fr
	if int(pagefr_e.get())>int(pageto_e.get()):
		pageto_e.set(pagefr_e.get())
	outputfilename()

### when pageto change, check if pageto is smaller than pagefr
def pagetochange(*evt): # will pass 3 parameters to function, use *evt to store for avoid error
	if int(totalPage_entry.get()) < 2: # if total page < 2, no need to do anything
		return
	if int(pageto_e.get())<int(pagefr_e.get()):
		pagefr_e.set(pageto_e.get())
	outputfilename()

### Output filename setting
def outputfilename():
	ori_fn_full = fileopen_location_entry.get()
	ori_fn = os.path.basename(ori_fn_full)
	folder_now = os.path.dirname(ori_fn_full)
	p_fr = "p" + str(pagefr_e.get())
	p_to = "p" + str(pageto_e.get())
	new_fn = ori_fn + "-" + p_fr + "_" + p_to + ".pdf"
	outfilename_entry.delete(0,END)
	outfilename_entry.insert(0, new_fn)
	outFolder_entry.delete(0,END)
	outFolder_entry.insert(0, folder_now)

### Open OUTPUT FOLDER
def outFolderLoc_extract():
	output_folder_extract = filedialog.askdirectory(title='OUTPUT LOCATION')
	if output_folder_extract != "":
		outFolder_entry.delete(0,END)
		outFolder_entry.insert(0,output_folder_extract)

### Extract the page(s) from PDF
def extractPDF():
	newPDFWriter = PdfFileWriter()
	pgfr2e = pagefr_e.get()-1
	pgto2e = pageto_e.get()
	for i in range(pgfr2e, pgto2e):
		newPDFWriter.addPage(pdfReader.getPage(i))
	outputfilename_full = outFolder_entry.get() + "/" + outfilename_entry.get()
	with open(outputfilename_full, 'wb') as f:
		newPDFWriter.write(f)
		f.close()

# define main window
guiWindow = tk.Tk()
guiWindow.title("PDF Editing (version: 0.1.227191")
guiWindow.geometry("500x500")
#guiWindow.iconbitmap('atn.ico')

# Main Container of tabs
pdf_tabControl = ttk.Notebook(guiWindow)

## create tab-instances
tab_1_merge = ttk.Frame(pdf_tabControl)
tab_2_extract = ttk.Frame(pdf_tabControl)
tab_3_splitRename = ttk.Frame(pdf_tabControl)
tab_4_readme = ttk.Frame(pdf_tabControl)

## add tab-instances to tab main container
pdf_tabControl.add(tab_1_merge, text="PDF Merge")
pdf_tabControl.add(tab_2_extract, text="PDF Extract")
pdf_tabControl.add(tab_4_readme, text="About")

## pack / grid the pdf_tabControl to guiWindow
pdf_tabControl.grid(row=0, column=0, padx=20, pady=10, sticky=N+W+E)

## Layout for PDF_MERGE
### declare variable for tkinter
mergeNot_1 = IntVar()
mergeNot_2 = IntVar()
mergeNot_3 = IntVar()
mergeNot_4 = IntVar()
mergeNot_5 = IntVar()
mergeNot_6 = IntVar()
mergeNot_7 = IntVar()
mergeNot_8 = IntVar()
mergeNot_9 = IntVar()
mergeNot_10 = IntVar()

## Frame for merge files
inputfiles_frame = Frame(tab_1_merge)
inputfiles_frame.grid(row=0, column=0, padx=10, pady=0, sticky=N+W+E)
	### frame contain main title
inputfile_title_frame = Frame(inputfiles_frame)
inputfile_title_frame.grid(row=0, column=0, padx=0, pady=0, sticky=N+W+E)
		#### Title for input file(s)
inputfile_title_label = Label(inputfile_title_frame, text="Files to be MERGED:")
inputfile_title_label.grid(row=0, column=0, padx=0, pady=10, sticky=N+W+E)
	### frame for table of files
files2merge_frame = Frame(inputfiles_frame)
files2merge_frame.grid(row=1, column=0, padx=0, pady=0, sticky=N+W+E)
		#### table list of files to be merged
# Header
fileMerge_Bool_0 = Label(files2merge_frame, text="Include?")
fileMerge_Bool_0.grid(row=0, column=0, padx=10, pady=0, sticky=N+W+E)
fileMerge_entry_0 = Label(files2merge_frame, text="File Path")
fileMerge_entry_0.grid(row=0, column=1, padx=10, pady=0, sticky=N+W+E)
fileMerge_btn_0 = Label(files2merge_frame, text="Browse")
fileMerge_btn_0.grid(row=0, column=2, padx=0, pady=0, sticky=N+W+E)
# file #1
fileMerge_Bool_1 = Checkbutton(files2merge_frame, text="#1", variable=mergeNot_1, onvalue=1, offvalue=0)
fileMerge_Bool_1.grid(row=1, column=0, padx=10, pady=0, sticky=N+W+E)
fileMerge_entry_1 = Entry(files2merge_frame, width=40, state="readonly")
fileMerge_entry_1.grid(row=1, column=1, padx=10, pady=0, sticky=N+W+E)
fileMerge_btn_1 = Button(files2merge_frame, text="SELECT", command=lambda:openfilepath_merge(1))
fileMerge_btn_1.grid(row=1, column=2, padx=0, pady=0, sticky=N+W+E)
# file #2
fileMerge_Bool_2 = Checkbutton(files2merge_frame, text="#2", variable=mergeNot_2, onvalue=1, offvalue=0)
fileMerge_Bool_2.grid(row=2, column=0, padx=10, pady=0, sticky=N+W+E)
fileMerge_entry_2 = Entry(files2merge_frame, width=40, state="readonly")
fileMerge_entry_2.grid(row=2, column=1, padx=10, pady=0, sticky=N+W+E)
fileMerge_btn_2 = Button(files2merge_frame, text="SELECT", command=lambda:openfilepath_merge(2))
fileMerge_btn_2.grid(row=2, column=2, padx=0, pady=0, sticky=N+W+E)
# file #3
fileMerge_Bool_3 = Checkbutton(files2merge_frame, text="#3", variable=mergeNot_3, onvalue=1, offvalue=0)
fileMerge_Bool_3.grid(row=3, column=0, padx=10, pady=0, sticky=N+W+E)
fileMerge_entry_3 = Entry(files2merge_frame, width=40, state="readonly")
fileMerge_entry_3.grid(row=3, column=1, padx=10, pady=0, sticky=N+W+E)
fileMerge_btn_3 = Button(files2merge_frame, text="SELECT", command=lambda:openfilepath_merge(3))
fileMerge_btn_3.grid(row=3, column=2, padx=0, pady=0, sticky=N+W+E)
# file #4
fileMerge_Bool_4 = Checkbutton(files2merge_frame, text="#4", variable=mergeNot_4, onvalue=1, offvalue=0)
fileMerge_Bool_4.grid(row=4, column=0, padx=10, pady=0, sticky=N+W+E)
fileMerge_entry_4 = Entry(files2merge_frame, width=40, state="readonly")
fileMerge_entry_4.grid(row=4, column=1, padx=10, pady=0, sticky=N+W+E)
fileMerge_btn_4 = Button(files2merge_frame, text="SELECT", command=lambda:openfilepath_merge(4))
fileMerge_btn_4.grid(row=4, column=2, padx=0, pady=0, sticky=N+W+E)
# file #5
fileMerge_Bool_5 = Checkbutton(files2merge_frame, text="#5", variable=mergeNot_5, onvalue=1, offvalue=0)
fileMerge_Bool_5.grid(row=5, column=0, padx=10, pady=0, sticky=N+W+E)
fileMerge_entry_5 = Entry(files2merge_frame, width=40, state="readonly")
fileMerge_entry_5.grid(row=5, column=1, padx=10, pady=0, sticky=N+W+E)
fileMerge_btn_5 = Button(files2merge_frame, text="SELECT", command=lambda:openfilepath_merge(5))
fileMerge_btn_5.grid(row=5, column=2, padx=0, pady=0, sticky=N+W+E)
# file #6
fileMerge_Bool_6 = Checkbutton(files2merge_frame, text="#6", variable=mergeNot_6, onvalue=1, offvalue=0)
fileMerge_Bool_6.grid(row=6, column=0, padx=10, pady=0, sticky=N+W+E)
fileMerge_entry_6 = Entry(files2merge_frame, width=40, state="readonly")
fileMerge_entry_6.grid(row=6, column=1, padx=10, pady=0, sticky=N+W+E)
fileMerge_btn_6 = Button(files2merge_frame, text="SELECT", command=lambda:openfilepath_merge(6))
fileMerge_btn_6.grid(row=6, column=2, padx=0, pady=0, sticky=N+W+E)
# file #7
fileMerge_Bool_7 = Checkbutton(files2merge_frame, text="#7", variable=mergeNot_7, onvalue=1, offvalue=0)
fileMerge_Bool_7.grid(row=7, column=0, padx=10, pady=0, sticky=N+W+E)
fileMerge_entry_7 = Entry(files2merge_frame, width=40, state="readonly")
fileMerge_entry_7.grid(row=7, column=1, padx=10, pady=0, sticky=N+W+E)
fileMerge_btn_7 = Button(files2merge_frame, text="SELECT", command=lambda:openfilepath_merge(7))
fileMerge_btn_7.grid(row=7, column=2, padx=0, pady=0, sticky=N+W+E)
# file #8
fileMerge_Bool_8 = Checkbutton(files2merge_frame, text="#8", variable=mergeNot_8, onvalue=1, offvalue=0)
fileMerge_Bool_8.grid(row=8, column=0, padx=10, pady=0, sticky=N+W+E)
fileMerge_entry_8 = Entry(files2merge_frame, width=40, state="readonly")
fileMerge_entry_8.grid(row=8, column=1, padx=10, pady=0, sticky=N+W+E)
fileMerge_btn_8 = Button(files2merge_frame, text="SELECT", command=lambda:openfilepath_merge(8))
fileMerge_btn_8.grid(row=8, column=2, padx=0, pady=0, sticky=N+W+E)
# file #9
fileMerge_Bool_9 = Checkbutton(files2merge_frame, text="#9", variable=mergeNot_9, onvalue=1, offvalue=0)
fileMerge_Bool_9.grid(row=9, column=0, padx=10, pady=0, sticky=N+W+E)
fileMerge_entry_9 = Entry(files2merge_frame, width=40, state="readonly")
fileMerge_entry_9.grid(row=9, column=1, padx=10, pady=0, sticky=N+W+E)
fileMerge_btn_9 = Button(files2merge_frame, text="SELECT", command=lambda:openfilepath_merge(9))
fileMerge_btn_9.grid(row=9, column=2, padx=0, pady=0, sticky=N+W+E)
# file #10
fileMerge_Bool_10 = Checkbutton(files2merge_frame, text="#10", variable=mergeNot_10, onvalue=1, offvalue=0)
fileMerge_Bool_10.grid(row=10, column=0, padx=10, pady=0, sticky=N+W+E)
fileMerge_entry_10 = Entry(files2merge_frame, width=40, state="readonly")
fileMerge_entry_10.grid(row=10, column=1, padx=10, pady=0, sticky=N+W+E)
fileMerge_btn_10 = Button(files2merge_frame, text="SELECT", command=lambda:openfilepath_merge(10))
fileMerge_btn_10.grid(row=10, column=2, padx=0, pady=0, sticky=N+W+E)

## frame for output folder and filename
output_file_frame_merge = Frame(tab_1_merge)
output_file_frame_merge.grid(row=2, column=0, padx=10, pady=10, sticky=N+W+E)
	### output file name
outfilename_label_merge = Label(output_file_frame_merge, text="Output File Name: ")
outfilename_label_merge.grid(row=0, column=0, padx=0, pady=0, sticky=N+E)
outfilename_entry_merge = Entry(output_file_frame_merge, width=30)
outfilename_entry_merge.grid(row=0, column=1, padx=0, pady=0, sticky=N+W+E)
outFolder_label_merge = Label(output_file_frame_merge, text="Output Folder: ")
outFolder_label_merge.grid(row=1, column=0, padx=0, pady=0, sticky=N+E)
outFolder_entry_merge = Entry(output_file_frame_merge)
outFolder_entry_merge.grid(row=1, column=1, padx=0, pady=0, sticky=N+W+E)
outFolder_btn_merge = Button(output_file_frame_merge, text="SAVE TO", command=outFolderLoc_merge)
outFolder_btn_merge.grid(row=1, column=2, padx=0, pady=0, sticky=N+W)

## Merge Button
merge_btn = Button(tab_1_merge, text="MERGE", command=mergePDF)
merge_btn.grid(row=3, column=0, padx=10, pady=10, sticky=N+W+E)

# Layout for PDF_Extract
## define variables for drop_down_menu
pagefr_e = IntVar()
pageto_e = IntVar()
pagefr_e.set(0)
pageto_e.set(0)
pagefr_range = [0]
pageto_range = [0]
pagefr_e.trace("w", pagefrchange)
pageto_e.trace("w", pagetochange)

## frame for file open dialog
fileopenFrame = Frame(tab_2_extract) # create a Frame inside tab_2_extract
fileopenFrame.grid(row=0, column=0, padx=10, pady=(10,0), sticky=W+N) # at the gird of tab_2_extract
### file to be open for extract
fileopen_location_label = Label(fileopenFrame, text="File for extract")
fileopen_location_label.grid(row=0, column=0, sticky=W, padx=20, pady=10)
fileopen_location_entry = Entry(fileopenFrame, width=30, state="readonly")
fileopen_location_entry.grid(row=0, column=1, sticky=W+E)
fileopen_location_btn = Button(fileopenFrame, text='SELECT', command=openfilepath_extract)
fileopen_location_btn.grid(row=0, column=2, sticky=E, padx=10)

## frame for page selection drop-down-menu
pagefrto_frame = Frame(tab_2_extract)
pagefrto_frame.grid(row=1, column=0, padx=10, pady=10, sticky=N+W+E)
### showing total Page
totalPage_label = Label(pagefrto_frame, text="Total Page(s): ")
totalPage_label.grid(row=0, column=0, padx=0, pady=0, sticky=N+W+E)
totalPage_entry = Entry(pagefrto_frame, width=10)
totalPage_entry.insert(0,0)
totalPage_entry.configure(state="readonly")
totalPage_entry.grid(row=0, column=1, padx=0, pady=0, sticky=N+W+E)
pagefr_label = Label(pagefrto_frame, text="From: ")
pagefr_label.grid(row=1, column=0, padx=0, pady=0, sticky=N+E)
pagefr_menu = OptionMenu(pagefrto_frame, pagefr_e, *pagefr_range)
#pagefr_menu.configure(state="disabled")
pagefr_menu.configure(width=10)
pagefr_menu.grid(row=1, column=1, padx=0, pady=0, sticky=N+W+E)
pageto_label = Label(pagefrto_frame, text="To: ")
pageto_label.grid(row=1, column=2, padx=0, pady=0, sticky=N+W+E)
pageto_menu = OptionMenu(pagefrto_frame, pageto_e, *pageto_range)
#pageto_menu.configure(state="disabled")
pageto_menu.configure(width=10)
pageto_menu.grid(row=1, column=3, padx=0, pady=0, sticky=N+W+E)

## frame for output folder and filename
output_file_frame = Frame(tab_2_extract)
output_file_frame.grid(row=2, column=0, padx=10, pady=10, sticky=N+W+E)
### output file name
outfilename_label = Label(output_file_frame, text="Output File Name: ")
outfilename_label.grid(row=0, column=0, padx=0, pady=0, sticky=N+E)
outfilename_entry = Entry(output_file_frame, width=30)
outfilename_entry.grid(row=0, column=1, padx=0, pady=0, sticky=N+W+E)
outFolder_label = Label(output_file_frame, text="Output Folder: ")
outFolder_label.grid(row=1, column=0, padx=0, pady=0, sticky=N+E)
outFolder_entry = Entry(output_file_frame)
outFolder_entry.grid(row=1, column=1, padx=0, pady=0, sticky=N+W+E)
outFolder_btn = Button(output_file_frame, text="SAVE TO", command=outFolderLoc_extract)
outFolder_btn.grid(row=1, column=2, padx=0, pady=0, sticky=N+W)

## Extract Button
extract_btn = Button(tab_2_extract, text="EXTRACT", command=extractPDF)
extract_btn.grid(row=3, column=0, padx=10, pady=10, sticky=N+W+E)

# Layout for README
## Frame for README
readme_text_content = '''
This is the first trial of PDF Editing function.

The editing may NOT work for "LOCKED" PDF file!!!


For more details, please visit:

https://github.com/thomaspkng/python_pdf_editing
'''
readme_box_frame = Frame(tab_4_readme)
readme_box_frame.grid(row=0, column=0, padx=10, pady=10, sticky=N+W+E)
readme_text_box = Text(readme_box_frame, width=48, height=25)
readme_text_box.grid(row=0, column=0, padx=0, pady=0, sticky=N+W+E)
readme_text_box.insert("end", readme_text_content)
readme_text_box.config(state='disabled')


guiWindow.mainloop()

# pyinstaller --onefile -- windowed --icon-atn.ico pdf_editing.py