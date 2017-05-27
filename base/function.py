#!/usr/bin/python3
# -*- coding: utf-8 -*-

n1 = 255
n2 = 1000
print('n1 = %s, n2 = %s' % (hex(n1), hex(n2)))

import math

def quadratic(a, b, c):
    if a == 0 and b != 0:
        return -c/b
    elif b*b-4*a*c > 0:
        return (-b+math.sqrt(b*b-4*a*c))/(2*a), (-b-math.sqrt(b*b-4*a*c))/(2*a)
    else:
        return 'no jie'

print(quadratic(int(input('a = ')),int(input('b = ')),int(input('c = '))))

