#!/usr/bin/python3
# -*- coding: utf-8 -*-

# '''1
import urllib.request

response = urllib.request.urlopen('https://account.douban.com/login')
print(response.read())
# '''

'''2
import urllib.request
import urllib.parse

values = {'username':'36283902@qq.com', 'password':'xxx'}
data = urllib.parse.urlencode(values)
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
req = urllib.request.Request(url, data.encode(encoding='utf-8'))
res = urllib.request.urlopen(req)
print(res.read())
'''

'''3
import urllib.request
import urllib.parse

values = {'username':'36283902@qq.com', 'password':'xxx'}
data = urllib.parse.urlencode(values)
url = 'https://passport.csdn.net/account/login'
geturl = url+'?'+data
req = urllib.request.Request(geturl)
res = urllib.request.urlopen(req)
print(res.read())
'''

'''4
import urllib.request
import urllib.error

request = urllib.request.Request('http://www.xxxxx.com')
try:
    urllib.request.urlopen(request)
except urllib.error.HTTPError as e:
    print('%s(%s)' % (e.reason, e.code))
except urllib.error.URLError as e:
    print('%s(%s)' % (e.reason, e.code))
else:
    print('ok')
'''

'''5
import urllib.request
import urllib.parse
import http.cookiejar

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print('Name = %s' % (item.name))
    print('Value = %s' % (item.value))
'''

'''6
import urllib.request
import urllib.parse
import http.cookiejar

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
hander = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(hander)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
'''

'''7
import urllib.request
import urllib.parse
import http.cookiejar

cookie = http.cookiejar.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
req = urllib.request.Request('http://www.baidu.com')
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
response = opener.open(req)
print(response.read())
'''

'''8 problem CSDN有个流水号的字段，所以登录不上去
import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
#req = urllib.request.Request('http://oa-center/Programs/login/login.aspx')
req = urllib.request.Request('https://passport.csdn.net/account/login')
postdata = urllib.parse.urlencode({
    'username':'daigouwei@sina.com',
    'password':'guowei911122'
    })
try:
    response = opener.open(req, postdata.encode(encoding='utf-8'))
except urllib.error.HTTPError as e:
    print('%s, %s' % (e.reason, e.code))
else:
    print('ok')
finally:
    print('finally')
cookie.save(ignore_discard=True, ignore_expires=True)
#reqgz = urllib.request.Request('http://oa-center/default.aspx')
reqgz = urllib.request.Request('http://my.csdn.net')
result = opener.open(reqgz, postdata.encode(encoding='utf-8'))
print(result.read())
'''
