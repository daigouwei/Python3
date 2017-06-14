#!/usr/bin/env
#-*- coding:utf-8 -*-

import re

def testValue():
    filteredWords = ['北京', '程序员', '公务员', '领导', '牛比', '牛逼', '你娘', '你妈', 'love', 'sex', 'jiangge']
    # while True:
        # word = input('input your word: ')
        # pattern = re.compile(r'.*?%s.*?' % filteredWords[0], re.S)
        # if re.search(pattern, word):
            # print('Freedom')
        # else:
            # print('Human Right')
    while True:
        FreedomFlag = False
        word = input('input your word: ')
        if word == 'q' or word == 'Q':
            break
        for sf in filteredWords:
            pattern = re.compile(r'.*?%s.*?' % sf, re.S)
            if re.search(pattern, word):
                FreedomFlag = True
                print('Freedom')
                break
        if not FreedomFlag:
            print('Human Right')

if __name__ == '__main__':
    testValue()
