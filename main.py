import numpy as np
import time
import pandas as pd

f = ['cs_170_small80.txt','cs_170_large80.txt']
class Classifier:
    def train(self,fname):
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
    def test(self,orig,cols):
        x = orig.loc[:,cols]
        x = np.array(x)
        dist = np.zeros((x.shape[0],x.shape[0]))
        for i in range(dist.shape[0]):
            for j in range(dist.shape[0]):
                dist[i][j] = np.linalg.norm(x[i]- x[j])
                if i == j:
                    dist[i][j] = np.Inf
        return dist
    def __init__(self,fname):
            self.x,self.y = self.train(fname)
            self.dist = self.test(self.x,[3,5,7])

class Validator:
    def leave_one_out_validation(self,dist,y):
        print(type(dist))
        if len(dist.shape[1]) == 0:
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
    def __init__(dist,y):
        self.acc = self.leave_one_out_validation(self,dist,y)
c = Classifier(f[0])
c.test(c.dist)
