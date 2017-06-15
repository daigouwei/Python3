#!/usr/bin/env
#-*- coding:utf-8 -*-

import re

def testValue():
    filteredWords = ['北京', '程序员', '公务员', '领导', '牛比', '牛逼', '你娘', '你妈', 'love', 'sex', 'jiangge']
    while True:
        word = input('input your word: ')
        if word == 'q' or word == 'Q':
            break
        for sf in filteredWords:
            pattern = re.compile(r'(%s)' % sf, re.S)
            word = re.sub(pattern, r'*'*len(sf), word)
        print(word)

if __name__ == '__main__':
    testValue()
