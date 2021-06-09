import numpy as np
import time
import pandas as pd

f = ['cs_170_small80.txt','cs_170_large80.txt']
def parse_test(fname):
    with open(fname,"r") as myfile:
        data = myfile.readlines()
    for i in range(len(data)):
        data[i] = data[i].split()
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = float(data[i][j])
            if j == 0:
                data[i][j] = int(data[i][j])
    data = pd.DataFrame(data)
    #drop class label from x and create y
    x = data.drop(0,axis = 1)
    y = data[0]

    #normalize data
    x = (x - x.mean() / x.std())
    return x,y
print(parse_test(f[0]))
