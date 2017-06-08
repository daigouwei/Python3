#!/usr/bin/env
#-*- coding:utf-8 -*-

import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

url = input('input your url:')
username = input('input your username:')
password = input('input your password:')
overtimeReason = input('input your overtimeReason:')

browser = webdriver.PhantomJS()
# browser = webdriver.Chrome()
browser.get(url)

#登录账号，后期还需要对输错密码进行处理
browser.find_element_by_name('tbUserName').send_keys(username)
browser.find_element_by_name('tbPassword').send_keys(password)
browser.find_element_by_name('btnLogin').click()
# print(browser.page_source)

#切换frame，点击进入考勤统计
browser.switch_to_frame('contents')
browser.find_element_by_id('a1').click()

#切换到main frame
browser.switch_to_default_content()
browser.switch_to_frame('main')

#提取date week firsttime lasttime信息并进行处理
soup = BeautifulSoup(browser.page_source, 'lxml')
soupStr = soup.find_all(id="GridViewPUNCH_CARD_INFO")
overtimeData = re.findall(re.compile(r'<span id="GridViewPUNCH_CARD_INFO_ctl.*?_lblKQ_DATE">(.*?)</span>.*?<span id="GridViewPUNCH_CARD_INFO_ctl.*?_lblWEEK">(.*?)</span>.*?<span id="GridViewPUNCH_CARD_INFO_ctl.*?_LabelPUNCH_CARD_FIRST_TIME_CAL">(.*?)</span>.*?<span id="GridViewPUNCH_CARD_INFO_ctl.*?_LabelPUNCH_CARD_LAST_TIME_CAL">(.*?)</span>', re.S), str(soupStr))
# print(overtimeData)
es = []
overtimeDataHandle = []
for sf in overtimeData:
    es = []
    if not (sf[2]=='' or sf[3]==''):
        if int(sf[0].split('-', 2)[2])>9:
            es.append(sf[0].split('-', 2)[2])
        else:
            es.append(sf[0].split('-', 2)[2][1])
        if not (sf[1]=='六' or sf[1]=='日'):
            es.append('18:30')
        else:
            if int(sf[2][3:5])>=30:
                es.append(sf[2][:2] + ':30')
            else:
                es.append(sf[2][:2] + ':00')
        if not sf[3]=='':
            if int(sf[3][3:5])>=30:
                es.append(str(int(sf[3][:2])+1) + ':00')
            else:
                es.append(sf[3][:2] + ':30')
        else:
            es.append('')
        if not (sf[1]=='六' or sf[1]=='日'):
            # if es[2]!='' and es[2]!='18:00' and es[2]!='18:30':
            if es[2]!='' and int(es[2][:2])>18:
                overtimeDataHandle.append(es)
        else:
            overtimeDataHandle.append(es)
print(overtimeDataHandle)

#切换frame点击进入加班申请
browser.switch_to_default_content()
browser.switch_to_frame('contents')
browser.find_element_by_id('a4').click()

#进行具体加班申请操作，解析日历等
browser.switch_to_default_content()
browser.switch_to_frame('main')
browser.find_element_by_id('TextBoxDATE_FROM').click() #点击起始日期
browser.switch_to_frame('CalFrame') #切换frame进入日历
browser.find_element_by_xpath(r'//img[@src="prev.gif"]').click() #点击日历中上个月箭头
soup = BeautifulSoup(browser.page_source, 'lxml')
calendarLists = soup.find_all('td', bgcolor='white')
# print(calendarLists)
calendarDict = {}
for calendarList in calendarLists:
    data = re.findall(re.compile(r'<td bgcolor="white" class="dt" id="(.*?)" style="font-weight: bold; cursor: pointer; color:.*?;">(.*?)</td>', re.S), str(calendarList))
    calendarDict[data[0][1]] = data[0][0]
print(calendarDict)
firstOvertimeFlag = True
for qop in overtimeDataHandle:
    if not firstOvertimeFlag:
        # browser.switch_to_default_content()
        # browser.switch_to_frame('main')
        browser.find_element_by_id('btnNew').click() #dianji xinjianshenqing anniu  diyicibuyongdianji
        browser.find_element_by_name('TextBoxREASON').send_keys(overtimeReason) #jiabanshiyou
        browser.find_element_by_id('TextBoxDATE_FROM').click() #qishiriqi dianji
        browser.switch_to_frame('CalFrame') #qiehuan frame jinrurili
        # # browser.find_element_by_xpath(r'//img[@src="prev.gif"]').click() #xuanzhongshanggeyue jiantou dianji
        browser.find_element_by_id(calendarDict[qop[0]]).click()
        browser.switch_to_default_content()
        browser.switch_to_frame('main')
        browser.find_element_by_id('TextBoxDATE_TO').click()
        browser.switch_to_frame('CalFrame') #qiehuan frame jinrurili
        # # browser.find_element_by_xpath(r'//img[@src="prev.gif"]').click() #xuanzhongshanggeyue jiantou dianji
        browser.find_element_by_id(calendarDict[qop[0]]).click()
        browser.switch_to_default_content()
        browser.switch_to_frame('main')
        selectTimeFrom = Select(browser.find_element_by_name('DropDownListTIME_FROM'))
        selectTimeFrom.select_by_visible_text(qop[1])
        selectTimeFrom = Select(browser.find_element_by_name('DropDownListTIME_TO'))
        selectTimeFrom.select_by_visible_text(qop[2])
        browser.find_element_by_id('btnAddLine').click()  #tianjiamingxi
        # browser.find_element_by_id('btnPost').click()  #tijiao
        time.sleep(10)
        browser.find_element_by_id('btnCancel').click()  #quxiaoshenqing
        time.sleep(3)
    else:
        firstOvertimeFlag = False
        browser.find_element_by_id(calendarDict[qop[0]]).click()
        browser.switch_to_default_content()
        browser.switch_to_frame('main')
        browser.find_element_by_name('TextBoxREASON').send_keys(overtimeReason) #jiabanshiyou
        browser.find_element_by_id('TextBoxDATE_TO').click()
        browser.switch_to_frame('CalFrame') #qiehuan frame jinrurili
        # # browser.find_element_by_xpath(r'//img[@src="prev.gif"]').click() #xuanzhongshanggeyue jiantou dianji
        browser.find_element_by_id(calendarDict[qop[0]]).click()
        browser.switch_to_default_content()
        browser.switch_to_frame('main')
        selectTimeFrom = Select(browser.find_element_by_name('DropDownListTIME_FROM'))
        selectTimeFrom.select_by_visible_text(qop[1])
        selectTimeFrom = Select(browser.find_element_by_name('DropDownListTIME_TO'))
        selectTimeFrom.select_by_visible_text(qop[2])
        browser.find_element_by_id('btnAddLine').click()  #tianjiamingxi
        # browser.find_element_by_id('btnPost').click()  #tijiao
        time.sleep(10)
        browser.find_element_by_id('btnCancel').click()  #quxiaoshenqing
        time.sleep(3)
browser.quit()
