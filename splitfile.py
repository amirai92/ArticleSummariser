from datetime import datetime
import logging
import os

import re
pathsections = "DataSet/Sections"
text=[]

"""

        doc_splitter = re.compile(r"^(?:Section\ )?\d+[\.\d+]?", re.MULTILINE)
       starts = [match.span()[0] for match in doc_splitter.finditer(listToStr)] + [len(listToStr)]
       sections = [listToStr[starts[idx]:starts[idx + 1]] for idx in range(len(starts) - 1)]
"""


def readData():
    doc_splitter = re.compile(r"^(?:Section\ )?\d+[\.\d+]?", re.MULTILINE)



    for file in os.listdir(pathsections):
        full_path = os.path.join(pathsections, file)
        if os.path.isfile(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                sections= []
                text= []
                listToStr= ""
                text.append((f.read()))
                listToStr = ' '.join([str(elem) for elem in text])


                starts = [match.span()[0] for match in doc_splitter.finditer(listToStr)] + [len(listToStr)]
                sections = [listToStr[starts[idx]:starts[idx + 1]] for idx in range(len(starts) - 1)]

                for i, name in enumerate(sections):
                    f = open(file + str(i + 1) + ".txt", "w",encoding='utf-8')

                    f.write(name + "\n")
                    f.close()

                #PathSections = os.path.join(pathsections, file)
                #oldfile = open(PathSections, 'w', encoding="utf-8")
                #oldfile.write(sections)




if __name__ == "__main__":
    readData()



