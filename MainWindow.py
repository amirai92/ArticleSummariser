import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import *
from shutil import copyfile

import graphviz
from PIL import ImageTk,Image
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
window.title("Summaryzer")
window.geometry("800x600")
window.config(background='black')
style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn' )



# TAB LAYOUT
tab_control = ttk.Notebook(window, style='lefttab.TNotebook')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

# ADD TABS TO NOTEBOOK
tab_control.add(tab2, text=f'{"File":^21s}')
tab_control.add(tab1, text=f'{"About":^20s}')



label1 = Label(tab1, text='Academic Article Summarizer ', padx=5, pady=5)
label1.grid(column=0, row=0)

#label2 = Label(tab2, text='Load File', padx=5, pady=5)
#label2.grid(column=0, row=0)



tab_control.pack(expand=1, fill='both')



# Functions
def openfiles():
    try:
        os.mkdir(r"DataSet/Sections")
        messagebox.showinfo("Directory","Created new directory")
    except OSError:
        messagebox.showerror("Directory", "Creation of the directory failed" )

    filename = filedialog.askopenfilename(initialdir=pathtext, title="Select A File",filetypes=(("Text files", ".txt"),("All Files" ,"*.* ")))
    show_file_name= filename.split('/')
    show_file_name = show_file_name[-1]
    messagebox.showerror("File","The file:\n %s loaded successfully." %show_file_name)
    read_text = open(filename, "r", encoding="utf-8" ).read()
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
    for file in os.listdir(section_path):
        full_path = os.path.join(section_path, file)
    with open(full_path, "r", encoding="utf-8") as f:
        for i, name in enumerate(save_file_name):
            if len(save_file_name) < i + 2:
                break
            elif i==0:
                G.node(save_file_name[i])

            else:
                G.node(save_file_name[i])
                G.edge(save_file_name[i], save_file_name[i + 1], constraint='true')

        G.view(directory=tree_path)
    b5.config(state=tk.ACTIVE)
    #b2.config(state=tk.ACTIVE)

def splited_files():

    filename = filedialog.askopenfilename(initialdir=pathsections, title="Select A File",filetypes=(("Splitied Text files", ".txt"),("All Files" ,"*.* ")))
   # read_text = open(filename, "r", encoding="utf-8").read()

    with open(filename, "r", encoding="utf-8") as f:
        data = []
        data.append((f.read()))
        listToStr = ""
        listToStr = ' '.join([str(elem) for elem in data])
        model = Summarizer()
        result = model(listToStr, min_length=60)
        full = ''.join(result)
        #bert_path = os.path.join(bertPath, file)
        #oldfile = open(bert_path, 'w', encoding="utf-8")
        #oldfile.write(full)
    result = '\nSummary:{}'.format(full)
    tab2_display_text.insert(tk.END, result)
    b3.config(state=tk.ACTIVE)
   # b2.config(state=tk.ACTIVE)

    #displayed_file.insert(tk.END, full)





def clear_text_result():
    tab2_display_text.delete('1.0', END)
    shutil.rmtree(pathsections)
    b5.config(state=tk.ACTIVE)


# Clear Text  with position 1.0
def clear_text_file():
    displayed_file.delete('1.0', END)
    shutil.rmtree(pathsections)
    b5.config(state=tk.ACTIVE)








# FILE PROCESSING TAB
#l1 = Label(tab2, text="The Whole File Text:")
#l1.grid(row=1, column=1)

displayed_file = ScrolledText(tab2, height=7)  # Initial was Text(tab2)
displayed_file.config(state=DISABLED)
displayed_file.grid(row=2, column=0, columnspan=3, padx=5, pady=3)

# BUTTONS FOR FILE READING TAB
b0 = Button(tab2, text="Load File", width=12, command=openfiles, bg='#c5cae9')
b0.grid(row=3, column=0, padx=10, pady=10)

b1 = Button(tab2, text="Reset ", width=12, command=clear_text_file, bg="#b9f6ca")
b1.grid(row=3, column=1, padx=10, pady=10)

#b2 = Button(tab2, text="Load Tree visualization", width=20, command=load_tree,bg="#b9f6ca" ,state=tk.DISABLED)
#b2.grid(row=5, column=2, padx=10, pady=10)

b3 = Button(tab2, text="Clear Result", width=12, command=clear_text_result, state=tk.DISABLED)
b3.grid(row=5, column=1, padx=10, pady=10)

b4 = Button(tab2, text="Close", width=12, command=window.destroy)
b4.grid(row=3, column=2, padx=10, pady=10)

b5 = Button(tab2, text="Summarize the splitied file  ", width=18 , command=splited_files, state=tk.DISABLED )
b5.grid(row=5, column=0, padx=10, pady=10)

# Display Screen
# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2, height=10)
tab2_display_text.config(state=DISABLED)
tab2_display_text.grid(row=7, column=0, columnspan=3, padx=5, pady=5)


#Create text box for About:
quote = """Have you ever encountered a situation where you had to scroll through a 400-word
article only to realize that there were only a few key points in the article?
We were all there.
In this age of information, when content is being created every second around the world,
it becomes quite difficult to extract the most important information in an optimal period of time, 
as the information we accumulate is only growing.
In recent years, advances and developments in machine learning and deep learning techniques
have paved the way and will be a future breakthrough,
therefore in this project the system that will help all kind of users 
to automatically summarize sections within academic article.


Version 0.1 Amir Aizin"""
tab1_display_text = ScrolledText(tab1, height=13,font='bold,20')

tab1_display_text.insert(tk.END, quote)
tab1_display_text.config(state=DISABLED)
tab1_display_text.grid(row=7, column=0, columnspan=3, padx=5, pady=5)







def get_filenames():
    path = "DataSet/TXT/"
    return os.listdir(path)

window.mainloop()
