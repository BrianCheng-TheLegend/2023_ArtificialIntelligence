import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Decision tree
class Decision_tree:
    def __init__(self,file_name):
        self.data=Data_preprocessing(file_name)
        
    def CreateTree(self):
        print('hi')
# train
## this part will calculate own gini by it own
# test


#data preprocessing for this dataset
class Data_preprocessing:
    def __init__(self,file_name):
        self.original_data = pd.read_csv(file_name)
        self.data=self.original_data.copy()
        self.Change_head(self.data)

    
    # remove the space in str to aviod error message
    def Change_head(self,data):
        new_colums ={ title: title.replace(' ','')for title in data.head()}
        data.rename(columns=new_colums,inplace=True)
    
    # calculate the gini impurity
    def Gini_impurity(self,column):
        P=column.value_counts()/column.shape[0]
        Gini=1-np.sum(P**2)
        return Gini



if __name__ == '__main__':
    pre_data=Data_preprocessing('train.csv')
    # print(pre_data.data.shape)