# from sklearn import datasets
# iris = datasets.load_iris()

from numpy import *

import matplotlib.pyplot as plt
import operator

class knn1:

    @classmethod
    def createDataSet(cls):
        group=array([[1, 1.1], [1, 1], [0, 0], [0, 0.1]])
        label=['a', 'a', 'b', 'a']
        return group,label

    @classmethod
    def classify0(cls,testset,dataSet,labels,k):
        dataSetSize = dataSet.shape[0]
        diffMat = tile(testset, (dataSetSize, 1)) - dataSet
        sqDiffMat = diffMat ** 2
        sqDistances = sqDiffMat.sum(axis=1)
        distances = sqDistances ** 0.5
        sortedDistIndicies = distances.argsort()
        classCount = {}
        for i in range(k):
            voteIlabel = labels[sortedDistIndicies[i]]
            classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]

    @classmethod
    def file2matrix(cls,filename):
        fp=open(filename)
        numberoflines=len(fp.readlines())
        returnmat=zeros((numberoflines,3))
        classlabelvector=[]
        returnmat=array(returnmat)

        fp = open(filename)
        index=0

        for line in fp.readlines():
            line = line.strip()
            listofline=line.split('\t')
            returnmat[index,:]=listofline[0:3]
            classlabelvector.append(int (listofline[-1]))
            index+=1
        return returnmat,classlabelvector

if __name__=="__main__":
    #group, labels= knn1.createDataSet()

    #print knn1.classify0([0,0],group,labels,1)

    group, labels =knn1.file2matrix("datingTestSet2.txt")
    print knn1.classify0([5569,4.875435,0.728658], group, labels, 1)