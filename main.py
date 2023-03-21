from tkinter import *
# import filedialog module
from tkinter import filedialog
import os
from PIL import ImageTk,Image
import glob
from PyPDF2 import PdfFileMerger
import os.path
from os import path
import pathlib
import random
from tkinter import ttk  



root = Tk()
# now root.geometry() returns valid size/placement
root.minsize(root.winfo_width(), root.winfo_height())
root.geometry("700x400")
root.title('pdf converter')

def con():
	filename = filedialog.askopenfilename(
    
    	initialdir = "C:/",
        title = "Select a File",
        filetypes = (('jpg', '*.jpg*'), ("png","*.png*")))

	if filename == '':
		return ''

	label_file_explorer.configure(text="File Opened: "+filename)
      
    

	im = Image.open(filename)
	im = im.convert('RGB')
	spleted = filename.split(sep='/')
	name_b4 = spleted[-1]
	a = name_b4.split(sep='.')
	file_outputname = a[0]
	spleted.pop()
	output_path = '/'.join(spleted)
	output_place =  Label(root, text=f'your file is in {output_path}').place(x=160, y=300)
	im = im.save(f'{output_path}/{file_outputname}.pdf')

    

    
def con_mer():
	foldername = filedialog.askdirectory(initialdir = "C:/", title = "Select a File")
	if foldername == '':
		return ''
	x = 0
	d = foldername
	pdf_files = []
	folder = os.path.join(foldername, 'your pdf')

	if os.path.exists(folder) == False:
		os.makedirs(folder)	
	elif os.path.exists(folder):
		pass

	for path in os.listdir(d):
		full_path = os.path.join(d, path)
		if full_path.endswith('.png') or full_path.endswith('.jpg'):
			label_file_explorer.configure(text="File Opened: "+foldername)
			if os.path.isfile(full_path):
				x += 1
				y = (str(x))
				im = Image.open(full_path)
				im = im.convert('RGB')
				output_path = full_path
				filename1 = output_path.split(sep='\\', maxsplit=2)[-1]
				filename = (filename1.split(sep='.')[0])
				output_place =  Label(root, text=f'your file is in {folder}').place(x=160, y=300)
				im = im.save(f'{folder}/{filename}.pdf')
		else:
			continue
			



def con_mer21():
	foldername = filedialog.askdirectory(initialdir = "C:/", title = "Select a File")
	if foldername == '':
		return ''
	label_file_explorer.configure(text="File Opened: "+foldername)
	folder = os.path.join(foldername, 'your pdf')

	if os.path.exists(folder) == False:
		os.makedirs(folder)	
	elif os.path.exists(folder):
		pass

	pdfs_paths = []

	for path in os.listdir(foldername):
		full_path = os.path.join(foldername, path)
		if full_path.endswith('.png') or full_path.endswith('.jpg'):
			label_file_explorer.configure(text="File Opened: "+foldername)
			if os.path.isfile(full_path):
				im = Image.open(full_path)
				im = im.convert('RGB')
				output_path = full_path
				filename1 = output_path.split(sep='\\', maxsplit=2)[-1]
				filename = (filename1.split(sep='.')[0])
				output_place =  Label(root, text=f'your file is in {foldername}').place(x=160, y=300)
				im = im.save(f'{folder}/{filename}.pdf')
				outpath = f'{folder}/{filename}.pdf'
				output_place =  Label(root, text=f'your file is in {folder}').place(x=160, y=300)
				pdfs_paths.append(outpath)
		else:
			continue



	merger = PdfFileMerger()
	for pdfname in os.listdir(folder):
		full_path = os.path.join(folder, pdfname)
		merger.append(full_path)
	
	output_file = os.path.join(folder, 'output.pdf')
	merger.write(output_file)
	merger.close()

	for oldpdf in os.listdir(folder):
		if  oldpdf != 'output.pdf':
			delete_path = os.path.join(folder, oldpdf)
			os.remove(delete_path)




def mer():

	foldername = filedialog.askdirectory(initialdir = "C:/", title = "Select a File")
	if foldername == '':
		return ''
	label_file_explorer.configure(text="File Opened: "+foldername)
	folder = os.path.join(foldername, 'your pdf')
	if os.path.exists(folder) == False:
		os.makedirs(folder)	
	elif os.path.exists(folder):
		pass

	merger = PdfFileMerger()
	for pdf in os.listdir(foldername):
		full_path = os.path.join(foldername, pdf)
		if full_path.endswith('.pdf'):
			merger.append(full_path)
		else:continue
	
	output_file = os.path.join(folder, 'output.pdf')
	output_place =  Label(root, text=f'your file is in {folder}').place(x=160, y=300)
	merger.write(output_file)
	merger.close()


         


variable = StringVar(root)
variable.set("nothing selected") 
the = variable.get()

def browse():
	the = variable.get()
	if the == 'images to multiple pdfs':
		con_mer()
	elif the == 'convert a single image':
		con()
	elif the == 'merage images into a pdf':
		con_mer21()
	elif the == 'merage pdfs':
		mer()
	elif the == 'nothing selected':
		label = Label(root, text='enter a input', fg='red').place(x=320, y=0)


intery = Label(root, text='input info type').place(x=235, y=24)

info = Label(root,fg = 'red', text='Nots: the output is gona be pdf - do not put any files in the folder that is gona be generated').place(x=112, y=340)

file_input = OptionMenu(root, variable, "images to multiple pdfs",  'merage images into a pdf', 'convert a single image', 'merage pdfs')
file_input.place(x=355, y=20)

# submit = Button(root, text='submit', command=browse, bg='light blue').place(x=325, y=100)


# do not forget to make it a folder and image checkbox
  
      
label_file_explorer = Label(root, text = "File Explorer using Tkinter",  fg = "blue")
                             
      
button_explore = Button(root,  text = "Browse Files", bg='light green', command = browse)
                         
button_explore.place(x=310,y=150)
label_file_explorer.place(x=280,y=200)  




  

root.mainloop()



