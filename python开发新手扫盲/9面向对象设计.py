class Triangle:
    classnum=0
    def __init__(self,x,y,z):
        self.a=x
        self.b=y
        self.c=z
        self.__color = 100
        self.price2 = 100


    def area(self):
        return 15

if __name__=="__main__":
    t1=Triangle(6,6,6)

    print t1.a,t1.b,t1.c,t1.area(),t1.price2,t1._Triangle__color
    print t1.classnum,t1.price2