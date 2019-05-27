#coding:utf8
#https://foofish.net/python-decorator.html


#1
# def foo():
#     print("foo")
#
# def bar(func):
#     func()
#
# bar(foo)

#2
# def use_logging(func):
#     print("%s is running" % func.__name__)
#     func()
#
# def foo():
#     print('i am foo')
#
# use_logging(foo)

#3
def use_logging(func):

    def wrapper(name):
        print("%s is running" % func.__name__)
        return func(name)   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

@use_logging
def foo(name):
    print('i am foo %s' %name)


foo('will')


#函数的导入
from pack1 import fun_a
print fun_a(1,3)


#sys,os

import os
#1 os.getcwd()
#2 os.listdir('.')

