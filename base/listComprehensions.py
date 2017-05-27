#!/usr/bin/python3
# -*- coding utf-8 -*-

#import os
#print([d for d in os.listdir('.')])

L1 = ['HELLO', 'WORLD', 18, 'APPLE', None]
print(L1)
L2 = [s.lower() if isinstance(s, str) else s for s in L1]
print(L2)
