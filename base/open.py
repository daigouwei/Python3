#!/usr/bin/python3
# -*- coding: utf-8 -*-

try:
    f = open('/root/tmp/python/helloworld.py', 'r')
    print(f.read())
finally:
    if f:
        f.close()
