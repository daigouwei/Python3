#!/usr/bin/python3
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import re

class DB:
    def __init__(self):
        self.loginURL = 'https://accounts.douban.com/login'
        self.loginURL_other = 'https://www.douban.com/accounts'
        self.loginMyUrl = 'https://www.douban.com/people/102499328/'
        self.proxyURL = 'http://100.103.106.76:8080'
        self.loginHeaders = {
            'Host': 'accounts.douban.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Referer': 'https://www.douban.com/accounts/login',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        self.username = 'yourmail'
        self.password = 'yourpassword'
        self.post = {
            'redir': 'https://www.douban.com',
            'form_email': self.username,
            'form_password': self.password,
            'login': '登录'
        }
        self.postData = urllib.parse.urlencode(self.post)
        self.proxy = urllib.request.ProxyHandler({'http':self.proxyURL})
        self.cookie = http.cookiejar.LWPCookieJar()
        self.cookieHandler = urllib.request.HTTPCookieProcessor(self.cookie)
        self.opener = urllib.request.build_opener(self.cookieHandler, self.proxy, urllib.request.HTTPHandler)

    def needIdenCode(self):
        request = urllib.request.Request(self.loginURL, self.postData.encode(encoding='utf-8'), self.loginHeaders)
        try:
            response = self.opener.open(request)
            content = response.read().decode('utf-8')
            print(content)
            # status = response.getcode()
            pattern = re.compile(r'<img id="captcha_image".*?src="(.*?)".*?>.*?<input type="hidden" name="captcha-id" value="(.*?)"/>', re.S)
            result = re.search(pattern, content)
            if result and result.group(1) and result.group(2):
                self.post['captcha-id'] = result.group(2)
                print('请打开网址： %s ,并输入网页中的验证码：' % result.group(1))
                checkcode = input()
                self.post['captcha-solution'] = checkcode
                self.postData = urllib.parse.urlencode(self.post)
                request1 = urllib.request.Request(self.loginURL_other, self.postData.encode(encoding='utf-8'), self.loginHeaders)
                response1 = self.opener.open(request1)
                content1 = response1.read().decode('utf-8')
                print(content1)
            else:
                print('有缓存不需要处理验证码')
        except urllib.error.URLError as e:
            print(e.reason)
        request2 = urllib.request.Request(self.loginMyUrl)
        response2 = self.opener.open(request2)
        content2 = response2.read().decode('utf-8')
        print(content2)


db = DB()
db.needIdenCode()
print('OVER')

