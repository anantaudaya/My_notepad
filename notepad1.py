from tkinter import *
from tkinter.messagebox import showinfo,askquestion
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os,time

def save_file():
    if file1!=None:
        value1 = askquestion("Notepad",f"Do you want to save changes to {file1} ?")
        if value1=="yes":
            f = open(file1, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            hhh="file saved sucesfully"
        else:
            hhh = "Ok chnges in previous file is not saved \n Now you can use the new file now "
        showinfo("Notepad",hhh)
def newfile():
    global file1
    root.title("Untitled - Notepad")
    save_file()
    file1 = None
    textarea.delete(1.0, END)

def openfile():
    global file1
    file1 = askopenfilename(filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if file1 == "":
        file1 = None
    else:
        root.title(os.path.basename(file1) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file1, "r")
        textarea.insert(1.0, f.read())
        f.close()

def savefile():
    global file1
    if file1 == None:
        file1 = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file1 =="":
            file1 = None
        else:
            f = open(file1, "w")
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file1) + " - Notepad")
            print("File Saved")
    else:
        f = open(file1, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def cut1():
    textarea.event_generate(("<<Cut>>"))

def copy1():
    textarea.event_generate(("<<Copy>>"))

def paste1():
    textarea.event_generate(("<<Paste>>"))
def aClear():
    global file1
    fil1=os.path.basename(file1)
    if file1!=None:
        if os.path.exists(fil1):
            os.remove(fil1)
    root.title("Untitled - Notepad")
    file1 = None
    textarea.delete(1.0, END)
    

def show1():
    showinfo("copyright","Notepad by Ananta Udaya Swain")

def callback(event):
    if textarea.get(1.0, END) == "Wellcome to Notepad\n":
        time.sleep(1)
        newfile()

def on_close():
    value12 = askquestion("Notepad",f"Do you want exit?")
    if file1==None and textarea.get(1.0,END)=="Wellcome to Notepad\n" or  len(textarea.get("1.0", END))==1:
        root.destroy()
    elif value12=="yes":
        value123 = askquestion("Notepad",f"Do you want save the recent file ?")
        if value123=="yes":
            savefile()
        root.destroy()

def Save_usins_ctrl(x):
    savefile()

if __name__=="__main__":
    root=Tk()
    root.title("My Notepad")
    root.iconbitmap("D:/python files/guiii/notepad_15342.ico")
    root.geometry("644x588")
    root.configure(bg="grey")

    textarea=Text(root)
    textarea.pack(expand=True,fill=BOTH)
    file1=None
    menubar=Menu(root)
    file_menu=Menu(menubar,tearoff=0)
    file_menu.add_command(label="New File",command= newfile)
    file_menu.add_command(label="Open File",command=openfile)
    file_menu.add_command(label="Save",command=savefile)
    file_menu.add_separator()
    file_menu.add_command(label="Exit",command= root.quit)
    menubar.add_cascade(label="File",menu=file_menu)
    
    edit_menu=Menu(menubar,tearoff=0)
    edit_menu.add_command(label="Cut",command= cut1)
    edit_menu.add_command(label="Copy",command=copy1)
    edit_menu.add_command(label="Paste",command=paste1)
    edit_menu.add_command(label='Delete', command = aClear)
    menubar.add_cascade(label="Edit",menu=edit_menu)
    

    help_menu=Menu(menubar,tearoff=0)
    help_menu.add_command(label="About",command=show1)
    menubar.add_cascade(label="help",menu=help_menu)

    root.config(menu=menubar)

    scroll = Scrollbar(textarea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command= textarea.yview)
    textarea.config(yscrollcommand = scroll.set)
    textarea.insert(1.0,"Wellcome to Notepad")
    textarea.bind( "<Button>", callback)

    root.protocol('WM_DELETE_WINDOW',on_close)
    root.bind("<Control-s>",Save_usins_ctrl)

    root.mainloop()

