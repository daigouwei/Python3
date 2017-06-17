#!/usr/bin/env
#-*- coding:utf-8 -*-

# 敏感词文本文件 filtered_words.txt，当用户输入敏感词语时，全部用*屏蔽，不敏感的词不屏蔽。

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
