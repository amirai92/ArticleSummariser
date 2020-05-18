"""
@author: Amir Aizin
Rouge matric calc:
"""

from matplotlib import pyplot


from rouge import FilesRouge, Rouge




files_rouge = FilesRouge()
rouge = Rouge()



"""
hyp - summary of the article 
ref - system output summary
"""





"""
hypothesis = '''
As the amount of available 3D models is constantly grow-
ing, systems that allow to organize and retrieve these models
are needed.  Recently, there has been an increasing interest
in the content-based description of 3D models with feature
vector transform (FT) algorithms to support similarity search
and  clustering  in  3D  databases  [TV04].   But,  as  has  been
observed earlier for other multimedia domains, and recently
also for the 3D domain [BKS⁺04], the suitability (effective-
ness) of different FTs depends heavily on the speciﬁc kind
(type,  class)  of  model_test  one  considers.   What  is  needed  are
interactive tools to assist the user in identifying and apply-
ing those FTs that serve her speciﬁc retrieval and clustering
tasks best.  Also welcome are solutions to quickly produce
summaries and overviews of large 3D databases.
'''

reference= " Multimedia objects are often described by high-dimensional feature vectors which can be used for retrieval and clustering tasks.  We have built an interactive retrieval system for 3D model_test databases that implements a variety of different fea-ture transforms. Recently, we have enhanced the functional-ity of our system by integrating a SOM-based visualization module. In this poster demo, we show how 2D maps can be used to improve the effectiveness of retrieval, clustering, and over-viewing tasks in a 3D multimedia system."
"""

ref_path = '/DataSet/SUM/2D_Maps_for_Visual_Analysis copy.txt'
print(type(ref_path))
hyp_path = '/DataSet/TXT/2D_Maps_for_Visual_Analysis.txt'

scores = rouge.get_scores(hyp_path, ref_path,avg=True)



print(scores)
