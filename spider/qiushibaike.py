#!/usr/bin/python3
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import urllib.error
import re

#糗事百科爬虫类
class QSBK:
    #初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.stories = []
        self.enable = False

    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/'+str(pageIndex)
            headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
            request = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                print('你长得太丑，连接段子失败，错误原因：%s' % e.reason)
                return None
        finally:
            pass

    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print('你长得太丑，页面加载失败...')
            return None
        pattern = re.compile(r'<div class="author clearfix">.*?<img.*?alt=(.*?)/>.*?<div class="content">(.*?)</div>(.*?)<i class="number">(.*?)</i>', re.S)
        items = re.findall(pattern, pageCode)
        pageStories = []
        for item in items:
            haveImg = re.search('img', item[2])
            if not haveImg:
                pageStories.append(item[1])
        return pageStories


    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    def getOnestory(self, pageStories, page):
        # print(pageStories)
        for story in pageStories:
            inputer = input()
            self.loadPage()
            if inputer == 'Q'or inputer == 'q':
                self.enable = False
                return
            # print('第%d页%s' % (page, story))
            print('%s' % (story))

    def start(self):
        print('正在读取段子，按回车继续，Q退出')
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOnestory(pageStories, nowPage)

spider = QSBK()
spider.start()
