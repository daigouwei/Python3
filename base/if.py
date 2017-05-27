#!/usr/bin/python3
# -*- coding: utf-8 -*-

s=input('shengao: ')
t=input('tizhong: ')
shengao=float(s)
tizhong=float(t)
x=tizhong/(shengao*shengao)
if x<18.5:
    print('1')
elif x>18.5 and x<25:
    print('2')
elif x>25 and x<28:
    print('3')
elif x>28 and x<32:
    print('4')
else:
    print('5')
