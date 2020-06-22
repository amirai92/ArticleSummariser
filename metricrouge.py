"""
@author: Amir Aizin
Rouge matric calc:
"""
import os
import logging
import sys
from datetime import datetime
import json
from tkinter import Entry, Tk, Label, NSEW, RIDGE, mainloop

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout
from matplotlib import pyplot as plt, pyplot
from matplotlib.pyplot import plot
from rouge import FilesRouge, Rouge
import pandas as pd
import numpy as np


handlers = [logging.StreamHandler()]
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s', datefmt="%H:%M:%S",
                    handlers=handlers)
# initialize dict's:
rouge_1_dct = {}
rouge_2_dct = {}
rouge_l_dct = {}
dct = {}
# Saving the F-Measure &Precision &Recall results:
rouge_1 = {"f": [], "p": [], "r": []}
rouge_2 = {"f": [], "p": [], "r": []}
rouge_l = {"f": [], "p": [], "r": []}
# Directory path:
ref_path = 'DataSet/Bert/'
hyp_path = 'DataSet/SUM/'
txtPath = "DataSet/TXT"
"""
Reference Summary (ref_path):'summary by humans'
System Summary (hyp_path):'summary from the machine'

"""


def calcRouge():
    for txtfile in os.listdir(txtPath):
        for reffile in os.listdir(ref_path):
            # in case file need to be splited:
            # txt_file_splitted = txtfile.split(".")[0]
            file_list = os.listdir(ref_path)
            try:
                if reffile in file_list:
                    for hypfile in os.listdir(hyp_path):
                        # in case file need to be splited:
                        # hyp_file_splitted = hypfile.split(" copy")[0]
                        if hypfile in file_list:
                            if hypfile == txtfile:
                                scores = rouge.get_scores(hypfile, reffile, avg=False)
                                dct[txtfile] = scores
                                break
            except OSError:
                print("File not found ")
    return dct


def move_to_dict(data):
    """
    :param data: json data , after calculate the metric rouge. the data located in (Rouge Results/rougeresult.json)
    :return: saving the data in dict's for each rouge
    """
    for file in data.keys():
        for rouge in data[file][0].keys():
            rouge_1_dct = data[file][0][rouge]
            rouge_2_dct = data[file][0][rouge]
            rouge_l_dct = data[file][0][rouge]
            for metric in data[file][0][rouge].keys():
                rouge_1_dct[metric] = data[file][0][rouge][metric]
                rouge_2_dct[metric] = data[file][0][rouge][metric]
                rouge_l_dct[metric] = data[file][0][rouge][metric]


def move_from_dict_to_plot(data):
    """
    :param data: data that been loaded from json file
    :return: reading the data and showing in plot
    """
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


def move_to_plot():
    """
    :return: the data showed in plot
    """
    # in case showing in plot:
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
    # in case working with text file:
    f = open("rougeresult.txt", "w")
    f.write(str(dct))
    f.close()







if __name__ == "__main__":
    startTime = datetime.now()
    logging.info("Script started")
    files_rouge = FilesRouge()
    rouge = Rouge()
    # dct=calcRouge()
    # saving the results to json file
    # with open('rougeresult.json', 'w') as json_file:
    #    json.dump(dct, json_file)
    with open('Rouge Results/rougeresult.json', 'r') as file:
        json_data = json.load(file)
    move_to_dict(json_data)
    move_from_dict_to_plot(json_data)
    #In case to show the results in plot
    #move_to_plot()
    logging.info("Script ended, execution time: " + str(datetime.now() - startTime))


