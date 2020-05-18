"""
@author: Amir Aizin
"""
import logging
import os
from datetime import datetime
from importlib import reload
from summarizer import Summarizer

logging.getLogger().setLevel(logging.INFO)

# Variables:
PathText = 'DataSet/TXT'
data = []
listToStr = ""
bertPath = 'DataSet/Bert'



def readfile():
    """
    This function taking the text's and remove all the references.
    :return: file without reference.
    """
    logging.info("Started to read the data set")
    for file in os.listdir(PathText):
        full_path = os.path.join(PathText, file)
        if os.path.isfile(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                data.append((f.read()))
                listToStr = ' '.join([str(elem) for elem in data])
                x = listToStr.split(("References"))[0]
                f.close()
                oldfile = open(full_path, 'w', encoding="utf-8")

                oldfile.write(x)
                oldfile.close()


# readfile()


def bert_summarizer():
    """
    the function will recive a text file and will run the bert_summraizer
    :return: A summraized article , using bert method
    """
    logging.info("Starting to summarize the files :")
    for file in os.listdir(PathText):
        full_path = os.path.join(PathText, file)
        if os.path.isfile(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                data.append((f.read()))
                listToStr = ' '.join([str(elem) for elem in data])
                model = Summarizer()
                result = model(listToStr, min_length=60)
                full = ''.join(result)
                bert_path = os.path.join(bertPath, file)
                oldfile = open(bert_path, 'w', encoding="utf-8")
                oldfile.write(full)


def main():
    startTime = datetime.now()
    logging.info("Script started")
    bert_summarizer()
    logging.info("Script ended, execution time: " + str(datetime.now() - startTime))

if __name__ == "__main__":
    main()
