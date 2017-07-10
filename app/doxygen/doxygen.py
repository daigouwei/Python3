#!/usr/bin/env
#-*- coding:utf-8 -*-

# 进行doxygen风格的注释，主要是函数声明和定义。

import os
import re

#正则匹配
def regular(patternName):
    if patternName=='funcAll':
        pattern = re.compile(r'(^\S{2,10}\s+|^\S{2,10}\s+\S{2,10}\s+)(PRO_|pro_)(.*?)\(\s*(.*?)\s*\)(\n|;\n)', re.S)#读取每行并匹配函数整体
    elif patternName=='argAll':
        pattern = re.compile(r'.* (\*|)(\S{2,})', re.S)#匹配split好的参数，使用的是将参数取出之后split再正则匹配去除空格，更具有一般性
    return pattern

#实现函数定义和函数声明的注释
def annotation(filePath):
    f = open(filePath, 'r')
    data = f.readlines()#按行读取到list
    # print(data)
    count = 0#计数用来推动list的查找插入，避免重复
    argument = []
    argumentSplit = []
    for lineData in data[count:]:
        funcDataList = regular('funcAll').findall(lineData)
        if funcDataList:
            # print(funcDataList)
            if not funcDataList[0][0]=='return':#在pro或PRO开头的函数名还有一种可能是return，规避这种情况。不过正则表达式已经使用开头无空格规避了一次。
                # data.insert(count, '** This is an %s\n'%(funcDataList[0][1]+funcDataList[0][2]))
                # data[count:count] = ['/*!\n', '@brief %s\n'%(funcDataList[0][1]+funcDataList[0][2]), '\n', '@param\n', '\n', '//TODO:\n', '*/\n']#在list插入元素的两种写法
                data[count:count] = ['\n', '/*!\n', '    @brief %s\n'%(funcDataList[0][1]+funcDataList[0][2]), '\n']#挤压成切片进行插入
                count += 4#表示插入了几行
                if not (funcDataList[0][3]=='' or funcDataList[0][3]=='void'):#丢弃void参数
                    argument.append(funcDataList[0][3])
                    argumentSplit = argument[0].split(',')
                    # print(argumentSplit)
                    for arg in argumentSplit:
                        argList = regular('argAll').findall(arg)
                        data.insert(count, '    @param %s\n'%(argList[0][1]))
                        count += 1
                        # print(argList)
                    data.insert(count, '\n')
                    count += 1
                    del argument[:]
                data[count:count] = ['    //TODO:\n', '*/\n']
                count += 2
        count += 1#不管是否匹配到函数都要将list移位
    # print(data)
    f.close()
    f = open(filePath, 'w')
    f.writelines(data)#按行写入数据，好像是直接覆盖源文件
    f.close()

#获取当前目录下的所有子文件的绝对路径
def filePath():
    pwd = os.getcwd()
    for (dirpath, dirnames, filenames) in os.walk(pwd):
        for filename in filenames:
            filePath = os.path.join(dirpath, filename)
            annotation(filePath)



if __name__ == '__main__':
    filePath()
