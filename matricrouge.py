"""
@author: Amir Aizin
Rouge matric calc:
"""
import os
import logging
from datetime import datetime
import json
from matplotlib import pyplot as plt, pyplot
from matplotlib.pyplot import plot
from rouge import FilesRouge, Rouge
import pandas as pd
import numpy as np
#import matplotlib.pylab as plt


handlers = [logging.StreamHandler()]
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s', datefmt="%H:%M:%S",
                    handlers=handlers)
#initialize dict's:
rouge_1_dct = {}
rouge_2_dct = {}
rouge_l_dct = {}
dct = {}
#Saving the F-Measure &Precision &Recall results:
rouge_1 = {"f": [], "p": [], "r": []}
rouge_2 = {"f": [], "p": [], "r": []}
rouge_l = {"f": [], "p": [], "r": []}
#Directory path:
ref_path = 'DataSet/Bert/'
hyp_path = 'DataSet/SUM/'
txtPath = "DataSet/TXT"
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
                            scores = rouge.get_scores(hypfile, reffile, avg=False)
                            dct[txtfile] = scores
                            break
            else:
                print("File not found")
    return dct

def move_to_dict(data):

    for file in data.keys():
        for rouge in data[file][0].keys():
            rouge_1_dct = data[file][0][rouge]
            rouge_2_dct = data[file][0][rouge]
            rouge_l_dct = data[file][0][rouge]
            for metric in data[file][0][rouge].keys():
                rouge_1_dct['f'] = data[file][0][rouge]['f']
                rouge_1_dct['p'] = data[file][0][rouge]['p']
                rouge_1_dct['r'] = data[file][0][rouge]['r']
                rouge_2_dct['f'] = data[file][0][rouge]['f']
                rouge_2_dct['p'] = data[file][0][rouge]['p']
                rouge_2_dct['r'] = data[file][0][rouge]['r']
                rouge_l_dct['f'] = data[file][0][rouge]['f']
                rouge_l_dct['p'] = data[file][0][rouge]['p']
                rouge_l_dct['r'] = data[file][0][rouge]['r']




def move_from_dict_to_plot(data):
    for file in data.keys():
        for metric in data[file][0]["rouge-1"].keys():
            if metric == 'f':
                rouge_1[metric].append(data[file][0]["rouge-1"][metric])
            elif metric == 'p':
                rouge_1[metric].append(data[file][0]["rouge-1"][metric])
            elif metric == 'r':
                rouge_1[metric].append(data[file][0]["rouge-1"][metric])

    for file in data.keys():
        for metric in data[file][0]["rouge-2"].keys():
            if metric == 'f':
                rouge_2[metric].append(data[file][0]["rouge-2"][metric])
            elif metric == 'p':
                rouge_2[metric].append(data[file][0]["rouge-2"][metric])
            elif metric == 'r':
                rouge_2[metric].append(data[file][0]["rouge-2"][metric])

    for file in data.keys():
        for metric in data[file][0]["rouge-l"].keys():
            if metric == 'f':
                rouge_l[metric].append(data[file][0]["rouge-l"][metric])
            elif metric == 'p':
                rouge_l[metric].append(data[file][0]["rouge-l"][metric])
            elif metric == 'r':
                rouge_l[metric].append(data[file][0]["rouge-l"][metric])

if __name__ == "__main__":
    startTime = datetime.now()
    logging.info("Script started")
    files_rouge = FilesRouge()
    rouge = Rouge()

    dct=calcRouge()

    #saving the results to json file
    with open('rougeresult.json', 'w') as json_file:
        json.dump(dct, json_file)

    with open('rougeresult.json', 'r') as file:
        json_data = json.load(file)

    move_to_dict(json_data)
    move_from_dict_to_plot(json_data)


    plot(rouge_1['f'], label='F-Measure')
    plot(rouge_1['p'], label='Precision')
    plot(rouge_1['r'], label='Recall')
    pyplot.legend()
    pyplot.savefig("rouge_1_result.png")
    pyplot.show()




    plot(rouge_2['f'], label='F-Measure')
    plot(rouge_2['p'], label='Precision')
    plot(rouge_2['r'], label='Recall')

    plot(rouge_l['f'], label='F-Measure')
    plot(rouge_l['p'], label='Precision')
    plot(rouge_l['r'], label='Recall')


    #in case working with text file:
    f = open("rougeresult.txt", "w")
    f.write(str(dct))
    f.close()



    logging.info("Script ended, execution time: " + str(datetime.now() - startTime))


