#!/usr/bin/env
#-*- coding:utf-8 -*-

# 任一个英文的纯文本文件，统计其中的单词出现的个数。

def statisticsNum(file):
    with open(file, 'r') as f:
        string = f.read()
        print(string)
        num = 0
        for letter in string:
            if letter == ' ' or letter == '\n':
                num += 1
    return num+1

if __name__ == '__main__':
    num = statisticsNum('/Users/daigouwei/Downloads/day4.txt')
    print(num)
