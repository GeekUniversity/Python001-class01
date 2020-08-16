# Author Andy Fang
# -*- coding:utf-8 -*-

def squash(x):
    return x**3

m = map(squash,range(10))
for i in m:
    print (i)