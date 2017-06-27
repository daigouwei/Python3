#!/usr/bin/env
#-*- coding:utf-8 -*-

import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
response = requests.get(url, verify=False)
# print(response.text)
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
# print(stations)
pprint(dict(stations), indent=4)
