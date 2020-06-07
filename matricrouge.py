"""
@author: Amir Aizin
Rouge matric calc:
"""
import os
import logging
from datetime import datetime
from rouge import FilesRouge, Rouge

handlers = [logging.StreamHandler()]
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s', datefmt="%H:%M:%S",
                    handlers=handlers)


"""
Reference Summary (gold standard — usually by humans):
System Summary (what the machine produced):

"""


def calcRouge():
    for txtfile in os.listdir(txtPath):
        for reffile in os.listdir(ref_path):
            # in case file need to be splited:
            # txt_file_splitted = txtfile.split(".")[0]
            file_list = os.listdir(ref_path)
            if reffile in file_list:
                for hypfile in os.listdir(hyp_path):
                    # in case file need to be splited:
                    # hyp_file_splitted = hypfile.split(" copy")[0]
                    if hypfile in file_list:
                        if hypfile == txtfile:
                            scores = rouge.get_scores(hypfile, reffile, avg=True)
                            dct[txtfile] = scores
                            break



            else:
                print("File not found")


if __name__ == "__main__":
    startTime = datetime.now()
    logging.info("Script started")
    files_rouge = FilesRouge()
    rouge = Rouge()
    ref_path = 'DataSet/Bert/'
    hyp_path = 'DataSet/SUM/'
    txtPath = "DataSet/TXT"
    dct = {}
    calcRouge()
    logging.info("Script ended, execution time: " + str(datetime.now() - startTime))
    f = open("rougeresult.txt", "w")
    f.write(str(dct))
    f.close()
