#!/usr/bin/python3.4
#-*- coding:utf-8 -*-

# 在doxygen html中插入表格的自动打印格式

import sys
import codecs

#格式化表格以适应doxygen html风格格式
def table(filePath):
    # f = open(filePath, 'r')
    f = codecs.open(filePath, 'r', encoding='utf-8', errors='ignore')#有部分源文件用open会报错
    data = f.readlines()#按行读取到list
    # print(data)
    row_num = []
    # row_num_son = []   bug:和24行狼狈，list是一种变量，会不停的互相赋值。
    Flag = False
    for line_data in data:
        line_data_split = line_data.split('   ')
        # print(line_data_split)
        row_count = 0
        for row in line_data_split:
            if not Flag:
                # row_num.append(row_num_son)
                row_num.append([])
            row_num[row_count].append(len(row))
            row_count += 1
        Flag = True
    # print(row_num)
    line_len_max = []
    for row_num_index in row_num:
        line_len_max.append(max(row_num_index))
    row_all_index = len(line_len_max)
    # print(line_len_max)
    new_line_data = []
    new_data = []
    for line_data in data:
        line_data_split = line_data.split('\n')[0].split('   ')
        for row_index in range(row_all_index):
            if row_index == 0:
                new_line_data.append('  * |' + line_data_split[row_index] + ' ' * (line_len_max[row_index] - len(line_data_split[row_index]) + 1) )
            elif row_index == row_all_index - 1:
                new_line_data.append('|' + line_data_split[row_index] + ' ' * (line_len_max[row_index] - len(line_data_split[row_index]) + 1) + '|' + '\n')
            else:
                new_line_data.append('|' + line_data_split[row_index] + ' ' * (line_len_max[row_index] - len(line_data_split[row_index]) + 1))
            # print(new_line_data)
        new_data.append(''.join(new_line_data))
        del new_line_data[:]
    new_data.insert(1, '  * |' + ':---:|' * row_all_index + '\n')
    # print(new_data)
    f.close()
    f = open(filePath, 'w')
    f.writelines(new_data)#按行写入数据，是直接覆盖源文件
    f.close()

#解析命令行参数
def commandLine():
    for fileCount in range(1, len(sys.argv)):
        print('****************************************************************************')
        print('*               %s'%(sys.argv[fileCount]))
        print('****************************************************************************')
        table(sys.argv[fileCount])



if __name__ == '__main__':
    commandLine()
