import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
from sklearn import svm
from sklearn.grid_search import GridSearchCV
from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')


def preprocessing():
	data = pd.read_csv("/users/autkarsh/Downloads/FeatureVectors.csv")
	col_names = []
	i,till=0,0
	for i in range(5):
	    for a in range(65,91):
	        col_names.append(chr(a)+str(i))
	        till=till+1
	        if(till==data.shape[1]):
	            break;
	data = pd.read_csv("/users/autkarsh/Downloads/FeatureVectors.csv",names=col_names)
	data_label = pd.read_csv("/users/autkarsh/Downloads/ClassLabels.csv",names="Label")
	data_label=data_label.iloc[:,0]
	print(data_label.head())
	data1 = pd.concat([data,data_label],axis=1)
	print(data1.head())

preprocessing()

#def svm(sequence):
