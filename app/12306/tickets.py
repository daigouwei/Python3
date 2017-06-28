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
def log(func):
    def wrapper(*argv, **kw):
        print('###################################################')
        logging.warn(func.__name__)
        print('###################################################')
        return func(*argv, **kw)
    return wrapper

from docopt import docopt
from stations import stations
import requests
import re
@log
def commandLineInterface():
    arguments = docopt(__doc__)
    # print(arguments)
    fromStation = stations.get(arguments['<from>'])
    toStation = stations[arguments['<to>']]
    date = arguments['<date>']
    print(fromStation, toStation, date)
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, fromStation, toStation)
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, verify=False)
    # print(response.text)
    pattern = re.compile(r'\|预订\|.*?\|([A-Z][0-9]+)\|.*?\|.*?\|([A-Z]+)\|([A-Z]+)\|(\d{2}:\d{2})\|(\d{2}:\d{2})\|(\d{2}:\d{2})\|.*?\|\d{8}\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|([\u4e00-\u9fa5]|[0-9]+|)\|([\u4e00-\u9fa5]|[0-9]+|)\|.*?\|([\u4e00-\u9fa5]|[0-9]+|)\|.*?\|.*?\|([\u4e00-\u9fa5]|[0-9]+|)\|([\u4e00-\u9fa5]|[0-9]+|)\|([\u4e00-\u9fa5]|[0-9]+|)\|', re.S)
    data = pattern.findall(response.text)
    print(data)














if __name__ == '__main__':
    commandLineInterface()
