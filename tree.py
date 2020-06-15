import os
import graphviz

import os
import re

pathsections = "DataSet/Sections"
section_path = "DataSet/Sections"
tree_path = "DataSet/Tree"
text = []
save_file_name = []
list_to_str = ""



def readData():
    # split by regular expression
    doc_splitter = re.compile(r"^(?:Section\ )?\d+[\.\d+]?", re.MULTILINE)
    for file in os.listdir(pathsections):
        full_path = os.path.join(pathsections, file)
        if os.path.isfile(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
             #   sections = []
                text = []
              #  listToStr = ""
                text.append((f.read()))
                listToStr = ' '.join([str(elem) for elem in text])
                starts = [match.span()[0] for match in doc_splitter.finditer(listToStr)] + [len(listToStr)]
                sections = [listToStr[starts[idx]:starts[idx + 1]] for idx in range(len(starts) - 1)]
                for i, name in enumerate(sections):
                    #TODO: Save to another directory the files that been sectioned:
                    PathSections = os.path.join(pathsections, file)
                    f = open(PathSections + str(i + 1), "w", encoding='utf-8')
                    f.write(name + "\n")
                    f.close()

def splited_files_into_list(save_file_name=None):
    for file in os.listdir(pathsections):
        full_path = os.path.join(pathsections, file)
        if os.path.isfile(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                save_file_name.append((f.readline()))
                f.seek(0)
    save_file_name.sort()







def graph_viz():
  #  list_to_str = ' '.join([str(elem) for elem in save_file_name])
    G = graphviz.Digraph(name="Article Summarizer", node_attr={'shape': 'tab', 'fixedsize' :'False'})
    for file in os.listdir(section_path):
        full_path = os.path.join(section_path, file)
    with open(full_path, "r", encoding="utf-8") as f:
        for i,name in enumerate(save_file_name):
            if len(save_file_name) < i+2:
                break
            else:
                G.node(save_file_name[i])
                G.edge(save_file_name[i],save_file_name[i+1], constraint='true')
                G.view(directory=tree_path)


if __name__ == "__main__":
    #readData()
    splited_files_into_list(save_file_name)
    graph_viz()

