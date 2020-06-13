import os
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.scrolledtext import *

pathsections = "DataSet/Sections"
pathtext = "DataSet/TXT"
"""

# Structure and Layout

text=[]
window = Tk()
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
tab_control.add(tab1, text=f'{"Home":^20s}')
tab_control.add(tab2, text=f'{"File":^20s}')


label1 = Label(tab1, text='Academic Article Summarizer ', padx=5, pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab2, text='Load File', padx=5, pady=5)
label2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')



# Functions
def openfiles():
    filename = filedialog.askopenfilename(initialdir=pathtext, title="Select A File",filetypes=(("Text files", ".txt"),("All Files" ,"*.* ")))
    read_text = open(filename,"r", encoding="utf-8" ).read()
    displayed_file.insert(tk.END, read_text)


def split_file():
    #split by regular expression
    doc_splitter = re.compile(r"^(?:Section\ )?\d+[\.\d+]?", re.MULTILINE)
    for file in os.listdir(pathsections):
        full_path = os.path.join(pathsections, file)
        if os.path.isfile(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                sections = []
                text = []
                listToStr = ""
                text.append((f.read()))
                listToStr = ' '.join([str(elem) for elem in text])
                starts = [match.span()[0] for match in doc_splitter.finditer(listToStr)] + [len(listToStr)]
                sections = [listToStr[starts[idx]:starts[idx + 1]] for idx in range(len(starts) - 1)]
                for i, name in enumerate(sections):
                    PathSections = os.path.join(pathsections, file)
                    f = open(PathSections + str(i + 1), "w", encoding='utf-8')
                    f.write(name + "\n")
                    f.close()

def get_file_summary():
  raw_text = displayed_file.get('1.0', tk.END)
 # final_text = text_summarizer(raw_text)
  #result = '\nSummary:{}'.format(final_text)
  #tab2_display_text.insert(tk.END, result)

"""
"""

def get_summary():
  raw_text = str(entry.get('1.0', tk.END))
  final_text = text_summarizer(raw_text)
  print(final_text)
  result = '\nSummary:{}'.format(final_text)
  tab1_display.insert(tk.END, result)


"""
"""


def clear_text_result():
    tab2_display_text.delete('1.0', END)

# Clear Text  with position 1.0
def clear_text_file():
    displayed_file.delete('1.0', END)

# FILE PROCESSING TAB
l1 = Label(tab2, text="File Text:")
l1.grid(row=1, column=1)

displayed_file = ScrolledText(tab2, height=7)  # Initial was Text(tab2)
displayed_file.grid(row=2, column=0, columnspan=3, padx=5, pady=3)

# BUTTONS FOR FILE READING TAB
b0 = Button(tab2, text="Open File", width=12, command=openfiles, bg='#c5cae9')
b0.grid(row=3, column=0, padx=10, pady=10)

b1 = Button(tab2, text="Reset ", width=12, command=clear_text_file, bg="#b9f6ca")
b1.grid(row=3, column=1, padx=10, pady=10)

b2 = Button(tab2, text="Summarize", width=12, command=get_file_summary,bg="#b9f6ca" )
b2.grid(row=3, column=2, padx=10, pady=10)

b3 = Button(tab2, text="Clear Result", width=12, command=clear_text_result)
b3.grid(row=5, column=1, padx=10, pady=10)

b4 = Button(tab2, text="Close", width=12, command=window.destroy)
b4.grid(row=5, column=2, padx=10, pady=10)

b5 = Button(tab2, text="Split file ", width=12 , command=split_file)
b5.grid(row=5, column=0, padx=10, pady=10)


# Display Screen
# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2, height=10)
tab2_display_text.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)
# About TAB
about_label = Label(tab1,
                    text="Summaryzer GUI V.0.0.1 \n Amir Aizin \n ",
                    pady=5, padx=5)
about_label.grid(column=0, row=1)
"""
def get_filenames():
    path = "DataSet/TXT/"
    return os.listdir(path)

root = Tk()
l = Listbox(root, height=5)
l = Listbox(root, height=5)
l.grid(column=0, row=0, sticky=(N,W,E,S))
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=0, sticky=(N,S))
l['yscrollcommand'] = s.set
ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
for filename in get_filenames():
    print(filename)
    l.insert(END, filename)

root.mainloop()