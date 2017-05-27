#!/usr/bin/python3
# -*- coding: utf-8 -*-

def triangles(n):
    L = [1]
    for x in range(n):
        yield L
        L = [1]+[L[i]+L[i+1] for i in range(x)] + [1]

for i in triangles(10):
    print(i)
