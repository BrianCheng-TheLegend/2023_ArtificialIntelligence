import csv
import matplotlib.pyplot as plt
import numpy as np


class hi:
    def __init__(self,data):
        self.data=np.asarray(data)
        self.c =0
        self.end=len(self.data[0])

    def hihi(self):
        self.c+=1
        print(self.end)


file=open('train.csv')
reader = csv.reader(file)

a=hi(reader)
a.hihi()