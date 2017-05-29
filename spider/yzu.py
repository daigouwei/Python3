#!/usr/bin/env
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import re

class YZU:
    def __init__(self):
        self.loginURL = 'http://yjsglxt.yzu.edu.cn/pyxx/login.aspx'
        self.loginHeaders = {
            'Host':'yjsglxt.yzu.edu.cn',
            'Origin':'http://yjsglxt.yzu.edu.cn',
            'Referer':'http://yjsglxt.yzu.edu.cn/pyxx/login.aspx',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Mobile Safari/537.36'
        }
        self.username = 'M14790'
        self.password = '85477284'
        self.post = {
            '__VIEWSTATE':'/wEPDwUENTM4MWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFEmN0bDAwJEltYWdlQnV0dG9uMabuLwAAiYKU+1REmq/s3lojHl/Ytvy5hLayiQn8y3hy',
            'ctl00$txtusername':self.username,
            'ctl00$txtpassword':self.password,
            'ctl00$txtyzm':'2144',
            'ctl00$ImageButton1.x':'32',
            'ctl00$ImageButton1.y':'28'
        }
        self.postData = urllib.parse.urlencode(self.post)
        self.cookie = http.cookiejar.LWPCookieJar()
        self.cookieHandler = urllib.request.HTTPCookieProcessor(self.cookie)
        self.opener = urllib.request.build_opener(self.cookieHandler)

    def needIdenCode(self):
        request = urllib.request.Request(self.loginURL, self.postData.encode(encoding='utf-8'), self.loginHeaders)
        response = self.opener.open(request)
        content = response.read().decode('utf-8')
        status = response.getcode()
        pattern = re.compile(r'<img alt=".*?" id="myCode" style="cursor:pointer;" onclick="change.*?" src="(.*?)">', re.S)
        result = re.search(pattern, content)
        if result:
            print('请输入验证码')




        print(content)
        print(status)

yzu = YZU()
yzu.needIdenCode()

