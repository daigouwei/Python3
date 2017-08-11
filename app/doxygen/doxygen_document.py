#!/usr/bin/python3.4
#-*- coding:utf-8 -*-

# 将doxygen风格的注释生成网页document

import os
import sys
import codecs
import re

#正则匹配
def regular(patternName):
    if patternName=='funcAll':
        pattern = re.compile(r'(^\w{1,}|^\w{1,}\s+\w{1,})\s+(\*\w+|\w+)\s*\(\s*(.*?)\s*\)(\n|;\n)', re.S)#读取每行并匹配函数整体
    elif patternName=='argAll':
        pattern = re.compile(r'.* (\*|\**|)(\w{1,})', re.S)#匹配split好的参数，使用的是将参数取出之后split再正则匹配去除空格，更具有一般性
    return pattern

#实现函数定义和函数声明的document语法添加
def document(filePath):
    # f = open(filePath, 'r')
    f = codecs.open(filePath, 'r', encoding='utf-8', errors='ignore')#有部分源文件用open会报错
    data = f.readlines()#按行读取到list
    # print(data)
    count = 0#计数用来推动list的查找插入，避免重复
    argument = []
    argumentSplit = []
    for lineData in data[count:]:
        funcDataList = regular('funcAll').findall(lineData)
        if funcDataList:
            if not (funcDataList[0][0]=='return' or funcDataList[0][0]=='#define' or list(funcDataList[0])[0][0:7]=='typedef'):#开头还有3种可能是return,#define，typedef规避这种情况。不过正则表达式已经使用开头无空格规避了一次。
                # print(lineData)
                # print(funcDataList)
                if  not funcDataList[0][1][0]=='*':#用来处理函数名前面返回指针(*)的情况
                    funcname = funcDataList[0][1]
                else:
                    funcname = list(funcDataList[0])[1][1:]
                if (data[count-1] == '*/\n' or data[count-2] == '*/\n' or data[count-1] == ' */\n' or data[count-2] == ' */\n'):
                    for shiftIndex in range(1,20):
                        if data[count-shiftIndex] == '/*!\n' or data[count-shiftIndex] == '/**\n':
                            if filePath.split('/')[-1].split('_')[1] == 'sppc' or filePath.split('/')[-1].split('_')[1] == 'spps':
                                data[count-shiftIndex] = '/*! \ingroup bluetec_' + filePath.split('/')[-1].split('_')[0] + '_' + 'spp\n'
                            elif filePath.split('/')[-1].split('_')[1] == 'di' or filePath.split('/')[-1].split('_')[1] == 'dm':
                                data[count-shiftIndex] = '/*! \ingroup bluetec_' + filePath.split('/')[-1].split('_')[0] + '_' + 'didm\n'
                            else:
                                data[count-shiftIndex] = '/*! \ingroup bluetec_' + filePath.split('/')[-1].split('_')[0] + '_' + filePath.split('/')[-1].split('_')[1] + '\n'
                            print('  * - ' + funcname + '()')
                            break
                        if shiftIndex == 19:
                            print('[WARNING]查看函数' + funcname + '是否符合doxygen一般注释规范...')
                else:
                    print('[WARNING]查看函数' + funcname + '是否符合doxygen一般注释规范...')
        count += 1#不管是否匹配到函数都要将list移位
    # print(data)
    f.close()
    f = open(filePath, 'w')
    f.writelines(data)#按行写入数据，是直接覆盖源文件
    f.close()

#获取当前目录下的所有子文件的绝对路径!![暂时没有使用]
def filePath():
    pwd = os.getcwd()
    for (dirpath, dirnames, filenames) in os.walk(pwd):
        for filename in filenames:
            filePath = os.path.join(dirpath, filename)
            print(filePath)
            document(filePath)

#解析命令行参数
def commandLine():
    for fileCount in range(1, len(sys.argv)):
        print('****************************************************************************')
        print('*               %s'%(sys.argv[fileCount]))
        print('****************************************************************************')
        document(sys.argv[fileCount])



if __name__ == '__main__':
    commandLine()