#!/usr/bin/python3
# -*- coding: utf-8 -*-

#L = sum([1,2,3])
#print(L)
from functools import reduce

def prod(L):

    def mul(x,y):
        return x*y

    return reduce(mul, L)
print(prod([1,2,3,4,0x5]))
