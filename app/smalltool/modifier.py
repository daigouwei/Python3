#!/usr/bin/env
#-*- coding:utf-8 -*-

import subprocess
import os
import re

def autoAlter():
    folder = input('请输入文件夹路径： ')#'/Users/daigouwei/Downloads/两生花'
    name = input('请输入要修改成的电影名字： ')#'两生花'
    formatt = input('请输入电影格式： ') #'mp4'
    if not os.path.isdir(folder):
        print('没有该目录，请查实...')
        return
    pattern = re.compile(r'.*?%s(\d{2}).*?%s$' % (name, formatt), re.S)
    movieName = subprocess.check_output(['ls', folder]).decode()
    movieList = movieName.split('\n')
    for movie in movieList:
        if movie != '':
            result = pattern.search(movie)
            if result:
                subprocess.check_output(['sudo', 'mv', folder+'/'+movie, folder+'/'+name+result.group(1)+r'.'+formatt])
            else:
                print('该目录下有文件%s不匹配，确认修改请输入y:要被修改成文件名，不修改请输入n:' % movie)
                command = input()
                if command == 'n':
                    continue
                else:
                    subprocess.check_output(['sudo', 'mv', folder+'/'+movie, folder+'/'+command[2:]])
    print('大吉大利，今晚吃鸡...')

if __name__ == '__main__':
    autoAlter()



