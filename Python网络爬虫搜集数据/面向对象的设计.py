class A:

    @staticmethod
    def pp():
        print('fulei method')
    pass

class B(object):
    pass

class C(A):

    # @staticmethod
    # def pp():
    #     print('zilei method')

    pass

class D(B):
    pass

class Chinese(object):

    nation='China'

    def __init__(self,id,name):
        self._id=id
        self.__name=name

    def sayHi(self,msg):
        print self.__name,msg

if __name__=="__main__":
    dashen=Chinese(1,'dasheng')
    bajie=Chinese(2,'bajie')

    print(Chinese.nation)

    fu=A()
    zi=C()

    fu.pp()
    zi.pp()