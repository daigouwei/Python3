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

# import logging
from docopt import docopt
from stations import stations
import requests
import re
from prettytable import PrettyTable
from colorama import init,Fore

def log(func):
    def wrapper(*argv, **kw):
        # logging.warn(func.__name__)
        return func(*argv, **kw)
    return wrapper

@log
def getKey(dic, value):
    return [k for k,v in dic.items() if value == v]

@log
def drawColor(data, color):
    if color == 'red':
        return Fore.RED + data + Fore.RESET
    elif color == 'blue':
        return Fore.BLUE + data + Fore.RESET
    elif color == 'yellow':
        return Fore.YELLOW + data + Fore.RESET
    elif color == 'green':
        return Fore.GREEN + data + Fore.RESET
    elif color == 'cyan':
        return Fore.CYAN + data + Fore.RESET

@log
def handleData(data, option):
    newData = []
    lastNewData = []
    temp = []
    for sf in data:
        newData.append(list(sf))
    for sf in newData:
        del(sf[0])
    if option == '':
        lastNewData = newData
    else:
        for sf in newData:
            if sf[0][0].lower() in option:
                lastNewData.append(sf)
    # print(lastNewData)
    for sf in lastNewData:
        sf[1] = getKey(stations, sf[1])[0]
        sf[2] = getKey(stations, sf[2])[0]
        sf[5] = sf[5].replace(':','小时')+'分钟'
        for es in range(11):
            if sf[es]=='':
                sf[es]='--'
    for sf in lastNewData:
        temp.append(sf[10])
        temp.append(sf[9])
        temp.append(sf[6])
        temp.append(sf[8])
        temp.append(sf[7])
        for es in range(6,11):
            sf[es] = temp[es-6]
        del temp[:]
    # print(lastNewData)
    return lastNewData

@log
def prettyPrint(data):
    headline = '车次 出发站 到达站 出发时间 到达时间 历时 一等 二等 软座 硬座 无座'.split()
    pt = PrettyTable()
    pt._set_field_names(headline)
    for sf in data:
        # for es in range(1,5):
            # sf[es] = drawColor(sf[es], 'red')
        sf[0] = drawColor(sf[0], 'blue')
        sf[1] = drawColor(sf[1], 'red')
        sf[2] = drawColor(sf[2], 'green')
        sf[3] = drawColor(sf[3], 'red')
        sf[4] = drawColor(sf[4], 'green')
        sf[5] = drawColor(sf[5], 'yellow')
        # sf[7] = drawColor(sf[7], 'red')
        pt.add_row(sf)
    print(pt)

@log
def getWebData(date, fromStation, toStation):
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, fromStation, toStation)
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, verify=False)
    # print(response.text)
    pattern = re.compile(r'\|(预订|23:00-06:00系统维护时间)\|.*?\|([A-Z][0-9]+|[0-9]+)\|.*?\|.*?\|([A-Z]+)\|([A-Z]+)\|(\d{2}:\d{2})\|(\d{2}:\d{2})\|(\d{2}:\d{2})\|.*?\|\d{8}\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|([\u4e00-\u9fa5]|[0-9]+|)\|.*?\|([\u4e00-\u9fa5]|[0-9]+|)\|.*?\|.*?\|([\u4e00-\u9fa5]|[0-9]+|)\|([\u4e00-\u9fa5]|[0-9]+|)\|([\u4e00-\u9fa5]|[0-9]+|)\|', re.S)
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
    options = ''.join(getKey(arguments, True))
    # print(type(options))
    # print(options)
    init()
    lastNewData = handleData(getWebData(date, fromStation, toStation), options)
    return lastNewData





if __name__ == '__main__':
    lastNewData = commandLineInterface()
    prettyPrint(lastNewData)

