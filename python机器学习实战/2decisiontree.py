
# coding:utf8
#https://blog.csdn.net/jerry81333/article/details/53125197 原理

from math import log

class tree:

    @classmethod
    def createDataSet(cls):
        dataset=[[1,1,'yes'],
                 [1,1,'yes'],
                 [1,0,'no'],
                 [0,1,'no'],
                 [0,1,'no']]
        labels=['no surfacing','flipers']
        return dataset,labels


    @classmethod
    def calcshannonent(cls,dataset):
        numentries=len(dataset)
        labelcount={}

        for featvec in dataset:
            currentlabel=featvec[-1]
            if currentlabel not in labelcount.keys():
                labelcount[currentlabel]=0
                labelcount[currentlabel] +=1
        shannonent=0
        for key in labelcount:
            prob=float(labelcount[key])/numentries
            shannonent= shannonent -prob*log(prob,2)

        return shannonent



if __name__=="__main__":
    ds,lbs=tree.createDataSet()
    # print ds,lbs
    sh=tree.calcshannonent(ds)
    print ds
    ds[0][-1]='maybe'
    print ds[4][2]