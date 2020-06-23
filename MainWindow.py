"""
@author: Amir Aizin
The main script of the project include GUI,
loading splitted files into the system , then using BERT Summarizer on the specific splited file.

"""

import os
import shutil
import tkinter as tk
from distutils.version import LooseVersion, StrictVersion
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import *
from urllib import request
import graphviz
from PIL import ImageTk,Image
from pyqtgraph import canvas
from summarizer import Summarizer

pathsections = "DataSet/Sections"
pathtext = "DataSet/TXT"
save_file_name = []
tree_path = "Tree"
section_path = "DataSet/Sections"
text=[]


# Structure and Layout
window = Tk()
window.iconbitmap('Logo FinalProject.ico')
window.title("Academic Article Summaryzer")
window.geometry("1000x900")
#window['bg'] = 'blue'
#window.configure(background='blue')
style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn' )



# TAB LAYOUT
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

# ADD TABS TO NOTEBOOK
tab_control.add(tab2, text=f'{"File":^20s}')
tab_control.add(tab1, text=f'{"About":^20s}')



label1 = Label(tab1, text='Explain on the system :', font='Arial' ,padx=5, pady=5)
label1.grid(column=0, row=0)


label2 = Label(tab2, text='Loaded file contents : ',font='Arial', padx=5, pady=5)
#label2['bg'] = 'blue'
label2.grid(column=0, row=0,columnspan=1)

label3 = Label(tab2, text="Summarized text :", font='Arial', padx=5, pady=5)
label3.grid(column=0, row=9, columnspan=1)

tab_control.pack(expand=1, fill='both')



# Functions
def openfiles():
    #tab2_display_text.config(state=DISABLED)
    try:
        os.mkdir(r"DataSet/Sections")
        messagebox.showinfo("Directory","Created new directory.\nchoose a file to summarize")
    except OSError:
        messagebox.showerror("Directory", "Creation of the directory failed." )

    filename = filedialog.askopenfilename(initialdir=pathtext, title="Select A File",filetypes=(("Text files", ".txt"),("All Files" ,"*.* ")))
    show_file_name = filename.split('/')
    show_file_name = show_file_name[-1]
    messagebox.showerror("File", "The file:\n%s loaded and splitted successfully!\n" % show_file_name)
    read_text = open(filename, "r", encoding="utf-8").read()
    displayed_file.insert(tk.END, read_text)
    filename_splited= filename.split('/')

    new_path = "DataSet/Sections/"+filename_splited[-1]
    #split by regular expression
    doc_splitter = re.compile(r"^(?:Section\ )?\d+[\.\d+]?", re.MULTILINE)
    with open(filename,"r",encoding="utf-8") as f:
        read_file = f.read()
        with open(new_path ,"w",encoding="utf-8") as ff:
            ff.write(read_file)
            sections = []
            text = []
            text.append((f.read()))
            starts = [match.span()[0] for match in doc_splitter.finditer(read_file)] + [len(read_file)]
            sections = [read_file[starts[idx]:starts[idx + 1]] for idx in range(len(starts) - 1)]
            for i, name in enumerate(sections):
                split_file = new_path.split(sep='.txt')[0].split('/')[-1]
                split_file = split_file +"_"+ str(i + 1) + ".txt"
                with open(r"DataSet/Sections/"+ split_file, "w", encoding='utf-8') as f:
                    f.write(name + "\n")
            #save_file_name.append((f.readline()))
            #f.seek(0)
            #save_file_name.sort()

    #Sort the list
    for file in os.listdir(pathsections):
        full_path = os.path.join(pathsections, file)
        if os.path.isfile(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                save_file_name.append((f.readline()))
                f.seek(0)

    save_file_name.sort()
    #Create graph with visualization
    G = graphviz.Digraph(name="Article Hierarchy", node_attr={'shape': 'tab', 'fixedsize': 'False'})

    try:
        os.mkdir(r"Tree")
        print("Created Directory for Tree Hierarchy")
    except OSError:
        print("Couldn't Create Directory for Tree Hierarchy")


    for file in os.listdir(section_path):
        full_path = os.path.join(section_path, file)
    with open(full_path, "r", encoding="utf-8") as f:
        for i, name in enumerate(save_file_name):
            str1 = save_file_name[i][0]
            if len(save_file_name) < i + 2:
                break
            elif i == 0:
                G.node(save_file_name[i])
            #elif LooseVersion(str1) != LooseVersion(save_file_name[i + 1][0]):
            #        G.node(save_file_name[i +1])
            #        G.node(save_file_name[i] , save_file_name[ i +1 ])

            elif save_file_name[i][1] == '.' and save_file_name[i][2] != ' ' and save_file_name[i+1][2].isdigit() and LooseVersion(save_file_name[i][2]) < LooseVersion(save_file_name[i+1][2]):
                G.node(save_file_name[i])
                G.edge(save_file_name[i],save_file_name[i+1])
            else:
                G.node(save_file_name[0])
                G.edge(save_file_name[0], save_file_name[i + 1], constraint='true')
        G.view(directory=tree_path)
    b5.config(state=tk.ACTIVE)
    button_bonus.config(state=tk.ACTIVE)
    #b2.config(state=tk.ACTIVE)





def splited_files():
    filename = filedialog.askopenfilename(initialdir=pathsections, title="Select A File",filetypes=(("Splitied Text files", ".txt"),("All Files" ,"*.* ")))
    with open(filename, "r", encoding="utf-8") as f:
        data = []
        data.append((f.read()))
        listToStr = ""
        listToStr = ' '.join([str(elem) for elem in data])
        messagebox.showinfo("Processing","Processing the data..\nIt may take few seconds..")
        model = Summarizer()
        result = model(listToStr, min_length=val1)
        print("check if the button accept the right value",val1)
        full = ''.join(result)
        #bert_path = os.path.join(bertPath, file)
        #oldfile = open(bert_path, 'w', encoding="utf-8")
        #oldfile.write(full)
    result = 'Summary:{}'.format(full)
    tab2_display_text.insert(tk.END, result)
    #img = PhotoImage(file=r"Rouge Results/rouge-results.png")
   # canvas.create_image(20,20,anchor=NW,image=img)
    #b3.config(state=tk.ACTIVE)
    b5.config(state=tk.ACTIVE)
   # b2.config(state=tk.ACTIVE)
    #displayed_file.delete(1.0,END)
    #displayed_file.insert(tk.END,listToStr)
    #displayed_file.insert(tk.END, full)


def get_slider_value():
    global val1
    try:
        val1= slider_1.get()
    except:
        val1=25
        messagebox.showinfo("Error","Error occurred while setting minimum length,\nThe value been set to default value ")



#The top window
def clear_text_file():
    displayed_file.delete('1.0', END)
    tab2_display_text.delete('1.0', END)
    try:
        shutil.rmtree(pathsections)
        shutil.rmtree(tree_path)
    except:
            print("Couldn't remove the directory")
    b5.config(state=tk.DISABLED)
    button_bonus.config(state=tk.DISABLED)

"""
#The bottom window
def clear_text_result():
    tab2_display_text.delete('1.0', END)
    try:
        shutil.rmtree(pathsections)
    except:
        print("Couldn't remove the directory")
    b5.config(state=tk.DISABLED)
    b3.config(state=tk.DISABLED)
"""



#slider_1 = tk.Scale(window, from_=20, to=500, length=400, resolution=1, orient=tk.HORIZONTAL)
#slider_1.pack()


def popup_window():

    window = tk.Toplevel()
    global slider_1
    slider_1 = tk.Scale(window, from_=1, to=60, length=60, resolution=1, orient=tk.HORIZONTAL)
    slider_1.pack()



    button1 = tk.Button(window, text="Select", command=get_slider_value)
    button1.pack()

    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.pack(fill='x')


# FILE PROCESSING TAB
#l1 = Label(tab2, text="The Whole File Text:")
#l1.grid(row=1, column=1)

displayed_file = ScrolledText(tab2, height=15 ,width=100,font='Arial,bold,20')  # Initial was Text(tab2)
displayed_file.grid(row=2, column=0, columnspan=3, padx=5, pady=3)
#displayed_file.config(state=ACTIVE)

# BUTTONS FOR FILE READING TAB
b0 = Button(tab2, text="Load File", width=12, command=openfiles, bg='#c5cae9')
b0.grid(row=3, column=0, padx=10, pady=10)

b1 = Button(tab2, text="Reset ", width=12, command=clear_text_file, bg="#b9f6ca")
b1.grid(row=3, column=1, padx=10, pady=10)

#b2 = Button(tab2, text="Load Tree visualization", width=20, command=load_tree,bg="#b9f6ca" ,state=tk.DISABLED)
#b2.grid(row=5, column=2, padx=10, pady=10)



#b3 = Button(tab2, text="Clear Result", width=12, command=clear_text_result, state=tk.DISABLED)
#b3.grid(row=10, column=1, padx=10, pady=10)

b4 = Button(tab2, text="Close",width=12, command=window.destroy)
b4.grid(row=3, column=2, padx=11, pady=10)

b5 = Button(tab2, text="Summarize the splitied file  ", width=18, command=splited_files, state=tk.DISABLED )
b5.grid(row=16, column=1, padx=10, pady=10)

#create scale widget for bert summarizer min length
#slider1 = Scale(tab2, from_=20, to=500, length=400, resolution=1, orient=HORIZONTAL)
#slider1.grid()

button_bonus = tk.Button(tab2, text="Minimum Length",command=popup_window,state=DISABLED)
button_bonus.grid(row=16, column=0, padx=10, pady=10)



#button1 = Button(tab2, text="Select", command=get_slider_value)
#button1.grid(row=16, column=0, padx=10, pady=10)


# Display Screen
# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2, height=14,width=100, font='Arial,bold,20')
tab2_display_text.grid(row=15, column=0, columnspan=3, padx=5, pady=5)



#quote for about section:
quote = """In recent years, advances and developments in machine learning and deep learning techniques
have paved the way and will be a future breakthrough.
therefore in this project ,the system will help to all kind of users 
to automatically summarize sections within academic article.
Version 0.1"""
#Create text box for About:
tab1_display_text = ScrolledText(tab1, height=6 ,width=100,font='Arial,bold,26',)
photo = tk.PhotoImage(file="Logo FinalProject BIG.png")
about_label = tk.Label(tab1,image=photo)
about_label.grid(column=0, row=10,sticky="S,E")
tab1_display_text.insert(tk.END, quote)
tab1_display_text.config(state=DISABLED)
tab1_display_text.grid(row=7, column=0, columnspan=2, padx=5, pady=5)


def get_filenames():
    path = "DataSet/TXT/"
    return os.listdir(path)

window.mainloop()
