#!/usr/bin/python3
# -*- coding: utf-8 -*-

#def f(x):
#    return x*x
#r = map(f, list(range(1,10)))
#print(r)
#print(list(r))

def f(x):
    return x.capitalize()

L = map(f, ['GUOwei','wangsHUang','caoPenG'])
print(list(L))
