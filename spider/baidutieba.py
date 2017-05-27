#!/usr/bin/python3
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import re

class TOOL:
    def __init__(self):
        self.removeImg = re.compile(r'<img.*?>')
        self.removeAddr = re.compile(r'<a.*?>|</a>')
        self.replaceLine = re.compile(r'<tr>|<div>|</div>|</p>')
        self.replaceTD = re.compile(r'<td>')
        # self.replaceFront = re.compile(r' {7}')
        self.replaceBR = re.compile(r'<br><br>|<br>')
        self.removeExtraTag = re.compile(r'<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        # x = re.sub(self.replaceFront,"    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()

class BDTB:
    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)

    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            return response.read().decode('utf-8')
        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                print('连接百度贴吧失败，错误原因' % e.reason)
                return None
        finally:
            pass

    def getTitle(self, page):
        pattern = re.compile(r'<h3 class="core_title_txt.*?">(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1)
        else:
            return None

    def getPageNum(self, page):
        pattern = re.compile(r'<li class="l_reply_num".*?<span class="red">(.*?)</span>.*?</li>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1)
        else:
            return None

    def getContent(self, page):
        pattern = re.compile(r'<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        if items:
            return items
        else:
            return None

class FILEE(TOOL):
    def __init__(self):
        #注意当子类和父类都有init时，需要手动在子类init父类，否则父类的init不能用
        TOOL.__init__(self)
        self.filee = None
        self.defaultTitle = '百度贴吧'

    def setFileTitle(self, fileTitle):
        if fileTitle is not None:
            self.filee = open(fileTitle+'.txt','w+')
            # self.file.close()
        else:
            self.filee = open(self.defaultTitle+'.txt','w+')
            # self.file.close()

    def writeFile(self, content):
        global lou
        for item in content:
            self.filee.write('\n\n%s楼-------------------------------------------------------\n' % lou)
            self.filee.write(self.replace(item))
            lou += 1

    def closeFile(self):
        self.filee.close()


baseURL = input("请输入帖子地址：")
seeLZ = input("只看楼主请输入1：")
# baseURL = 'http://tieba.baidu.com/p/3138733512'
# seeLZ = 1

bdtb = BDTB(baseURL, seeLZ)
indexPage = bdtb.getPage(1)
title = bdtb.getTitle(indexPage)
filee = FILEE()
filee.setFileTitle(title)

lou = 1
pageNum = bdtb.getPageNum(indexPage)
print('该帖子共有%s页!' % pageNum)
for num in range(1, int(pageNum)+1):
    indexPage = bdtb.getPage(num)
    content = bdtb.getContent(indexPage)
    print('正在写入第%s页数据,稍安勿躁...' % num)
    filee.writeFile(content)
filee.closeFile()
print('写入任务完成，请尽情欣赏！')


