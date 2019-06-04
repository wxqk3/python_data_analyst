# -*- coding:utf8 -*-
#--------------------------总结
# by william xia, supported by 北风万视频
#第7章熟悉了

# break continue 高性能循环
#------------------------------

#1。

a=3

def change():
    print(123)
    a=2
    print(a)

change()
print a

# 1.变量作用域
# 1。1局部
a=3

def change():
    print(123)
    a=2
    print(a)

change()
print a



# 1。2 全局

a=3

def change():
    print(123)
    global a
    a=2
    print(a)

change()
print a
# 1。3 命名空间

#实战
def getsting(str):
    da=0
    xiao=0
    num=0
    other=0
    for s in str:
        if s >='a' and s<= 'z':
            xiao+=1
        elif s >='A' and s<= 'Z':
            da=da+1
        elif s>'0' and s<'9':
            num = num +1
        else: other=other+1


    return (xiao,da,num,other)



str=raw_input("str===?")
tup=getsting(str)
print tup