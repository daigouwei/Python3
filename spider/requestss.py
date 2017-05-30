#!/usr/bin/env
# -*- coding:utf-8 -*-

import requests

'''1
r = requests.get('http://cuiqingcai.com')
print(type(r))
print(r.status_code)
print(r.encoding)
print(r.cookies)
'''

'''2
r = requests.get('http://cuiqingcai.com/get', params={'key1':'value1', 'key2':'value2'}, headers={'content-type':'application/json'})
print(r.url)
'''

# '''3
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
# '''

# '''4
r1 = requests.get('https://kyfw.12306.cn/otn', verify=True)
print(r2.text)
r2 = requests.get('https://github.com', verify=True)
print(r2.text)

