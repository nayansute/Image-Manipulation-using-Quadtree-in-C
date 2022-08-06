import tkinter as tk
import subprocess
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo

#definitions

val = 0
textboxx = 0
f = 0
f1 = 0

def done():
	y = tk.Label(root, text="Process Done!!!", padx=10, pady=10, font=10, bg='wheat')
	y.pack(side='bottom')
	root.config()
	root.mainloop()

def getval():
	global val
	global textboxx
	global f
	val = textboxx.get(1.0, "end-1c")
	print(val, type(val))
	subprocess.call(["gcc", "quadtree.c"])
	tmp = subprocess.call(["./a.out", "-m", "c", val, f, "compress"+val+".ppm"])
	done()
	
	
def Compress():
	global textboxx
	global f
	textboxx = tk.Text(root, height=1, width=15)
	textboxx.place(x=180, y=180)
	f = str(fd.askopenfilename())
	butt = Button(root, text = "okk", command=getval)
	butt.place(x=200, y=210)
		
	
#Decompress
def decompress():
    f = str(fd.askopenfilename())
    subprocess.call(["gcc", "quadtree.c"])
    tmp=subprocess.call(["./a.out", "-d", f, "decom.ppm"])
    done()

def flipvv():
	global val
	global textboxx
	global f
	val = textboxx.get(1.0, "end-1c")
	print(val, type(val))
	subprocess.call(["gcc", "quadtree.c"])
	tmp=subprocess.call(["./a.out", "-m", "v", val, f, "ver"+val+".ppm"])
	done()

def flipv():
	global textboxx
	global f
	textboxx = tk.Text(root, height=1, width=15)
	textboxx.place(x=180, y=180)
	f = str(fd.askopenfilename())
	butt = Button(root, text = "okk", command=flipvv)
	butt.place(x=200, y=210)
	"""
    f = str(fd.askopenfilename())
    subprocess.call(["gcc", "quadtree.c"])
    tmp=subprocess.call(["./a.out", "-m", "v", "45", f, "ver.ppm"])
    y = tk.Label(root, text="Process Done!!!", padx=10, pady=10, font=10, bg='wheat')
    y.pack(side='bottom')
    root.config()
    root.mainloop()"""
    
def fliphh():
	global val
	global textboxx
	global f
	val = textboxx.get(1.0, "end-1c")
	print(val, type(val))
	subprocess.call(["gcc", "quadtree.c"])
	tmp=subprocess.call(["./a.out", "-m", "h", val, f, "hor"+val+".ppm"])
	done()

def fliph():
	global textboxx
	global f
	textboxx = tk.Text(root, height=1, width=15)
	textboxx.place(x=180, y=180)
	f = str(fd.askopenfilename())
	butt = Button(root, text = "okk", command=fliphh)
	butt.place(x=200, y=210)
	"""
    f = str(fd.askopenfilename())
    subprocess.call(["gcc", "quadtree.c"])
    tmp=subprocess.call(["./a.out", "-m", "h", "45", f, "hor.ppm"])
    y = tk.Label(root, text="Process Done!!!", padx=10, pady=10, font=10, bg='wheat')
    y.pack(side='bottom')
    root.config()
    root.mainloop()"""


def overlayy():
	global val
	global textboxx
	global f
	global f1
	val = textboxx.get(1.0, "end-1c")
	print(val, type(val))
	subprocess.call(["gcc", "quadtree.c"])
	tmp=subprocess.call(["./a.out", "-o", val, f, f1, "overlay"+val+".ppm"])
	done()

def overlay():
	global textboxx
	global f
	global f1
	textboxx = tk.Text(root, height=1, width=15)
	textboxx.place(x=180, y=180)
	f = str(fd.askopenfilename())
	f1 = str(fd.askopenfilename())
	butt = Button(root, text = "okk", command=overlayy)
	butt.place(x=200, y=210)
	"""
    f = str(fd.askopenfilename())
    g = str(fd.askopenfilename())
    subprocess.call(["gcc", "quadtree.c"])
    tmp=subprocess.call(["./a.out", "-o", "270", f, g, "overlay.ppm"])
    y = tk.Label(root, text="Process Done!!!", padx=10, pady=10, font=10, bg='wheat')
    y.pack(side='bottom')
    root.config()
    root.mainloop()"""

def getcommand():
    text = str(clicked.get())
    print(text)
    if(text=="Compress"):
        Compress()
    if(text=="Decompress"):
    	decompress()
    if(text=="Flip v"):
    	flipv()
    if(text=="Flip h"):
    	fliph()
    if(text=="Overlay"):
    	overlay()
  

root = Tk()
root.title("Menu")
root.geometry('500x500')

#Start

#Menu
menubar = Menu(root)
file = Menu(menubar, tearoff = 1)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...')
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)


edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)


help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Help', command = None)
help_.add_separator()
help_.add_command(label ='About')


#Selection
clicked = StringVar()
clicked.set("")
drop = OptionMenu(root, clicked, "Select the operation", "Compress","Decompress", "Flip v", "Flip h", "Overlay")
clicked = StringVar()
clicked.set("")
drop = OptionMenu(root, clicked, "Select the operation", "Compress", "Decompress", "Flip v", "Flip h", "Overlay")
drop.pack()

button = Button(root, text="OK", command=getcommand)
button.place(x=200, y=100)

#End and pack

root.config(menu=menubar, bg="wheat")
mainloop()
