#!/usr/bin/env
#-*- coding:utf-8 -*-

# 进行doxygen风格的注释，主要是函数声明和定义。

import os
from os import path
import re

def regular(patternName):
    if patternName=='funcAll':
        # pattern = re.compile(r'(^\S{2,10}\s+|^\S{2,10}\s+\S{2,10}\s+)(PRO_|pro_)(.*?)\(.*?\)(\n|;\n)', re.S)
        pattern = re.compile(r'(^\S{2,10}\s+|^\S{2,10}\s+\S{2,10}\s+)(PRO_|pro_)(.*?)\(\s*(.*?)\s*\)(\n|;\n)', re.S)
        # pattern = re.compile(r'(^\S{2,10}\s+|^\S{2,10}\s+\S{2,10}\s+)(PRO_|pro_)(.*?)\((.*?( .*?\s*,))*.*?( .*?)\s*\)(\n|;\n)', re.S)
    elif patternName=='argAll':
        pattern = re.compile(r'.* (\*|)(\S{2,})', re.S)
    return pattern

def annotation():
    f = open('test.c', 'r')
    data = f.readlines()
    # print(data)
    count = 0
    argument = []
    argumentSplit = []
    for lineData in data[count:]:
        funcDataList = regular('funcAll').findall(lineData)
        if funcDataList:
            # print(funcDataList)
            if not funcDataList[0][0]=='return':
                # data.insert(count, '** This is an %s\n'%(funcDataList[0][1]+funcDataList[0][2]))
                # data[count:count] = ['/*!\n', '@brief %s\n'%(funcDataList[0][1]+funcDataList[0][2]), '\n', '@param\n', '\n', '//TODO:\n', '*/\n']
                data[count:count] = ['\n', '/*!\n', '    @brief %s\n'%(funcDataList[0][1]+funcDataList[0][2]), '\n']
                count += 4#insert n line
                if not (funcDataList[0][3]=='' or funcDataList[0][3]=='void'):
                    argument.append(funcDataList[0][3])
                    argumentSplit = argument[0].split(',')
                    # print(argumentSplit)
                    for arg in argumentSplit:
                        argList = regular('argAll').findall(arg)
                        data.insert(count, '    @param %s\n'%(argList[0][1]))
                        count += 1
                        print(argList)
                    data.insert(count, '\n')
                    count += 1
                    del argument[:]
                data[count:count] = ['    //TODO:\n', '*/\n']
                count += 2
        count += 1#next
    # print(data)
    f.close()
    f = open('test.c', 'w')
    f.writelines(data)
    f.close()

if __name__ == '__main__':
    annotation()
