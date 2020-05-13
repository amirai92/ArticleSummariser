"""
@author: Amir Aizin
"""
import os
from importlib import reload
from summarizer import Summarizer

PathText = '/Users/Amir/PycharmProjects/FinalProject/DS/TXT'
data = []
listToStr=""


def readfile():
    """
    This function taking the text's and remove all the references.
    :return: file without reference.
    """
    for file in os.listdir(PathText):
        full_path = os.path.join(PathText, file)
        if os.path.isfile(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                data.append((f.read()))
                listToStr = ' '.join([str(elem) for elem in data])
                x=listToStr.split(("References"))[0]
                f.close()
                oldfile = open(full_path, 'w', encoding="utf-8")

                oldfile.write(x)
                oldfile.close()

#readfile()



def bert_summarizer():
    """
    the function will recive a text file and will run the bert_summraizer
    :return: A summraized article , using bert method
    """
    for file in os.listdir(PathText):
        full_path = os.path.join(PathText, file)
        if os.path.isfile(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                data.append((f.read()))
                listToStr = ' '.join([str(elem) for elem in data])
                model=Summarizer()
                result = model(listToStr, min_length=60, max_length=10000)
                full = ''.join(result)




bert_summarizer()

print("helo")




"""
body =

model = Summarizer()
result = model(body, min_length=60, max_length=10000)
full = ''.join(result)
"""
