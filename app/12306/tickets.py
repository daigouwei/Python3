#!/usr/bin/env
#-*- coding:utf-8 -*-

"""命令行火车票查看器
Usage:
    tickets.py [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets.py 北京 上海 2016-10-10
    tickets.py -dg 成都 南京 2016-10-10
"""

import logging
from docopt import docopt
from stations import stations
import requests
import re
from prettytable import PrettyTable

def log(func):
    def wrapper(*argv, **kw):
        logging.warn(func.__name__)
        return func(*argv, **kw)
    return wrapper

@log
def getKey(stations, value):
    return [k for k,v in stations.items() if value == v]

@log
def handleData(data):
    newData = []
    for sf in data:
        newData.append(list(sf))
    for sf in newData:
        sf[1] = getKey(stations, sf[1])[0]
        sf[2] = getKey(stations, sf[2])[0]
        sf[5] = sf[5].replace(':','h')+'min'
    return newData

@log
def prettyPrint(data):
    headline = '1 2 3 4 5 6 7 8 9 10 11 12'.split()
    pt = PrettyTable()
    pt._set_field_names(headline)
    for sf in data:
        pt.add_row(sf)
    print(pt)

@log
def getWebData(date, fromStation, toStation):
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, fromStation, toStation)
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, verify=False)
    # print(response.text)
    pattern = re.compile(r'\|预订\|.*?\|([A-Z][0-9]+)\|.*?\|.*?\|([A-Z]+)\|([A-Z]+)\|(\d{2}:\d{2})\|(\d{2}:\d{2})\|(\d{2}:\d{2})\|.*?\|\d{8}\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|([\u4e00-\u9fa5]|[0-9]+|)\|([\u4e00-\u9fa5]|[0-9]+|)\|.*?\|([\u4e00-\u9fa5]|[0-9]+|)\|.*?\|.*?\|([\u4e00-\u9fa5]|[0-9]+|)\|([\u4e00-\u9fa5]|[0-9]+|)\|([\u4e00-\u9fa5]|[0-9]+|)\|', re.S)
    data = pattern.findall(response.text)
    # print(data)
    return data

@log
def commandLineInterface():
    arguments = docopt(__doc__)
    # print(arguments)
    fromStation = stations.get(arguments['<from>'])
    toStation = stations[arguments['<to>']]
    date = arguments['<date>']
    # print(fromStation, toStation, date)
    newData = handleData(getWebData(date, fromStation, toStation))
    prettyPrint(newData)








if __name__ == '__main__':
    commandLineInterface()
