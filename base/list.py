#!/usr/bin/python3
# -*- coding: utf-8 -*-

#L=[
#        ['1','2','3'],
#        ['4','5','6'],
#        ['7','8','9']
#]
#print(L[0][0],  L[1][1],  L[2][2])
#print('hello')

L = []
n = 1
while n<100:
    L.append(n)
    n = n+2
#print(L)
r = []
n = 5
for i in range(n):
    r.append(L[i])
print(r[2])
print(r[-3:])
print(r[-3:-1])

