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

#create distance matrix
def create_distance_matrix(x):
    x = np.array(x)
    dist = np.zeros((x.shape[0],x.shape[0]))
    for i in range(dist.shape[0]):
        for j in range(dist.shape[0]):
            dist[i][j] = np.linalg.norm(x[i]- x[j])
            if i == j:
                dist[i][j] = np.Inf
    return dist

def validator(orig,y,cols):
    x = orig.loc[:,cols]
    if len(cols) == 0:
        return len(np.unique(y) ) ** -1
    #test the leave 1 out 
    total = 0
    correct = 0
    dist = create_distance_matrix(x)
    for i in range(y.shape[0]):
        minDist = np.argmin(dist[i])
        if y[minDist] == y[i]:
            correct +=1
        total+=1
    return correct / total

x,y = parse_test(f[1])
dist = create_distance_matrix(x)
r = validator(x,y,[1,15,27])
