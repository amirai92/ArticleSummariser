from datetime import datetime
import logging
import os
import re

pathsections = "DataSet/Sections"
text = []
save_file_name = []

"""
doc_splitter = re.compile(r"^(?:Section\ )?\d+[\.\d+]?", re.MULTILINE)
starts = [match.span()[0] for match in doc_splitter.finditer(listToStr)] + [len(listToStr)]
sections = [listToStr[starts[idx]:starts[idx + 1]] for idx in range(len(starts) - 1)]      
"""


def readData():
    # split by regular expression
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
                    split_file = file.split(sep='.')[0]
                    split_file = split_file + str(i + 1) + ".txt"
                    PathSections = os.path.join(pathsections, split_file)
                    f = open(PathSections , "w", encoding='utf-8')
                    f.write(name + "\n")
                    f.close()


def try_1(save_file_name=None):
    for file in os.listdir(pathsections):
        full_path = os.path.join(pathsections, file)
        if os.path.isfile(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                save_file_name.append((f.readline()))
                f.seek(0)
    save_file_name.sort()



if __name__ == "__main__":
    readData()
   # try_1(save_file_name)




