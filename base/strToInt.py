#!/usr/bin/python3
# -*- coding: utf-8 -*-

from functools import reduce

def strToInt(s):
    return reduce(lambda x,y:10*x+y, map(lambda x:{'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[x], s))

a = input('input a str: ')
print(strToInt(a))
