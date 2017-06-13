#!/usr/bin/env
#-*- coding:utf-8 -*-

import subprocess
import re
import os

class Mount:
    def __init__(self):
        self.devDict = {}

    def getDeviceNode(self):
        diskList = subprocess.check_output(['diskutil', 'list']).split('\n')
        for info in diskList:
            if re.search(re,compile(r'.*?NTFS.*?', re.S), info):
                infoList = info.split()
                diskPath = r'/Volumes/'+infoList[2]
                devNode = r'/dev/'+infoList[5]
                self.devDict[diskPath] = devNode

    def mountNtfs(self):
        if not self.devDict:
            print('No ntfs filesystem found...')
            return
        for diskPath in self.devDict:
            devNode = self.devDict[diskPath]
            if os.path.isdir(diskPath):
                subprocess.check_output(['hdiutil', 'detach', diskPath])
            print('mkdir %s' % diskPath)
            subprocess.check_output(['mkdir', diskPath])
            print('sudo mount_ntfs -o rw,nobrowse %s %s' % (devNode, diskPath))
            subprocess.check_output(['sudo',
                                    'mount_ntfs',
                                    '-o',
                                    'rw,nobrowse',
                                    devNode, diskPath])
            subprocess.check_output(['cd', diskPath])
            subprocess.check_output(['open', r'.'])

if __name__ == '__main__':
    mount = Mount()
    mount.getDeviceNode()
    mount.mountNtfs()

