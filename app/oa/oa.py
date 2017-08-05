#!/usr/bin/env
#-*- coding:utf-8 -*-

import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from prettytable import PrettyTable
import time

def commandLineInterface():
    url = 'http://172.26.10.41/Programs/login/login.aspx'
    username = input('请输入你的工号: ')
    password = input('请输入你的密码: ')

    #登录账号，后期还需要对输错密码进行处理
    # browser = webdriver.PhantomJS()
    browser = webdriver.Chrome()
    browser.get(url)
    browser.find_element_by_name('tbUserName').send_keys(username)
    browser.find_element_by_name('tbPassword').send_keys(password)
    browser.find_element_by_name('btnLogin').click()
    # print(browser.page_source)

    #提取date week firsttime lasttime信息并进行处理
    browser.switch_to_frame('contents') #切换frame，点击进入考勤统计
    browser.find_element_by_id('a1').click()
    browser.switch_to_default_content()
    browser.switch_to_frame('main') #切换到main frame,开始提取信息
    browser.find_element_by_id('RadioButtonPREV_MONTH').click()  #选中上月
    soup = BeautifulSoup(browser.page_source, 'lxml')
    soupStr = soup.find_all(id="GridViewPUNCH_CARD_INFO")
    overtimeData = re.findall(re.compile(r'<span id="GridViewPUNCH_CARD_INFO_ctl.*?_lblKQ_DATE">(.*?)</span>.*?<span id="GridViewPUNCH_CARD_INFO_ctl.*?_lblWEEK">(.*?)</span>.*?<span id="GridViewPUNCH_CARD_INFO_ctl.*?_LabelPUNCH_CARD_FIRST_TIME_CAL">(.*?)</span>.*?<span id="GridViewPUNCH_CARD_INFO_ctl.*?_LabelPUNCH_CARD_LAST_TIME_CAL">(.*?)</span>', re.S), str(soupStr))
    es = []
    overtimeDataHandle = []
    for sf in overtimeData:
        es = []
        if not (sf[2]=='' or sf[3]==''):
            if int(sf[0].split('-', 2)[2])>9:
                es.append(sf[0].split('-', 2)[2])
            else:
                es.append(sf[0].split('-', 2)[2][1])
            es.append(sf[1])     #增加星期几的信息，方便判断填入加班申请事由
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
                # if es[3]!='' and es[3]!='18:00' and es[3]!='18:30':
                if es[3]!='' and int(es[3][:2])>18:
                    overtimeDataHandle.append(es)
            else:
                overtimeDataHandle.append(es)
    # print(overtimeDataHandle)

    headline = '日期 星期 加班刷卡 下班刷卡'.split()
    pt = PrettyTable()
    pt._set_field_names(headline)
    for sf in overtimeDataHandle:
        pt.add_row(sf)
    print(pt)

    defaultReason = input('请输入懒人专属加班事由(下面直接回车的就会加载该默认加班事由): ')
    for sf in overtimeDataHandle:
        overtimeReason = input('请输入%s号的加班事由: ' % sf[0])
        if overtimeReason == '':
            sf.append(defaultReason)
        else:
            sf.append(overtimeReason)
    # print(overtimeDataHandle)

    headline = '日期 星期 加班刷卡 下班刷卡 加班事由'.split()
    pt = PrettyTable()
    pt._set_field_names(headline)
    for sf in overtimeDataHandle:
        pt.add_row(sf)
    print(pt)

    confirm = input('请对照上表确认无误，输入yes开始进行申请： ')
    if confirm == 'yes':
        #切换frame点击进入加班申请，解析日历等
        browser.switch_to_default_content()
        browser.switch_to_frame('contents')
        browser.find_element_by_id('a4').click()
        browser.switch_to_default_content()
        browser.switch_to_frame('main')
        browser.find_element_by_id('TextBoxDATE_FROM').click() #点击起始日期
        browser.switch_to_frame('CalFrame') #切换frame进入日历
        browser.find_element_by_xpath(r'//img[@src="prev.gif"]').click() #点击日历中上个月箭头切换至上个月的日历信息
        soup = BeautifulSoup(browser.page_source, 'lxml')
        calendarLists = soup.find_all('td', bgcolor='white')
        calendarDict = {}
        for calendarList in calendarLists:
            # data = re.findall(re.compile(r'<td bgcolor="white" class="dt" id="(.*?)" style="font-weight: bold; cursor: pointer; color:.*?; ">(.*?)</td>', re.S), str(calendarList)) #这是PhantomJS的正则
            data = re.findall(re.compile(r'<td bgcolor="white" class="dt" id="(.*?)" style="font-weight: bold; cursor: pointer; color:.*?;">(.*?)</td>', re.S), str(calendarList)) #这是chrome的正则，相差最后一个空格
            calendarDict[data[0][1]] = data[0][0]
        # print(calendarDict)

        #进行具体加班申请操作
        firstOvertimeFlag = True
        for qop in overtimeDataHandle:
            if not firstOvertimeFlag:
                browser.find_element_by_id('btnNew').click()  #点击新建申请
                browser.find_element_by_name('TextBoxREASON').send_keys(qop[4])  #输入加班事由
                browser.find_element_by_id('TextBoxDATE_FROM').click()  #点击起始日期
                browser.switch_to_frame('CalFrame')  #切换frame进入日历
                browser.find_element_by_xpath(r'//img[@src="prev.gif"]').click()  #点击日历中上个月箭头切换至上个月的日历信息
                browser.find_element_by_id(calendarDict[qop[0]]).click()
                browser.switch_to_default_content()
                browser.switch_to_frame('main')
                browser.find_element_by_id('TextBoxDATE_TO').click()
                browser.switch_to_frame('CalFrame')  #切换frame进入日历
                browser.find_element_by_xpath(r'//img[@src="prev.gif"]').click()  #点击日历中上个月箭头切换至上个月的日历信息
                browser.find_element_by_id(calendarDict[qop[0]]).click()
                browser.switch_to_default_content()
                browser.switch_to_frame('main')
                selectTimeFrom = Select(browser.find_element_by_name('DropDownListTIME_FROM'))
                selectTimeFrom.select_by_visible_text(qop[2])
                selectTimeTo = Select(browser.find_element_by_name('DropDownListTIME_TO'))
                selectTimeTo.select_by_visible_text(qop[3])
                # time.sleep(int(delaytime))
                browser.find_element_by_id('btnAddLine').click()  #添加明细
                time.sleep(3)  #延时，防止提交按钮丢失
                browser.find_element_by_id('btnPost').click()  #提交
                print('%s号加班申请完成...' % (qop[0]))
                # browser.find_element_by_id('btnCancel').click()  #取消申请
            else:
                firstOvertimeFlag = False
                browser.find_element_by_id(calendarDict[qop[0]]).click()
                browser.switch_to_default_content()
                browser.switch_to_frame('main')
                browser.find_element_by_name('TextBoxREASON').send_keys(qop[4])  #输入加班事由
                browser.find_element_by_id('TextBoxDATE_TO').click()
                browser.switch_to_frame('CalFrame')  #切换frame进入日历
                browser.find_element_by_xpath(r'//img[@src="prev.gif"]').click()  #点击日历中上个月箭头切换至上个月的日历信息
                browser.find_element_by_id(calendarDict[qop[0]]).click()
                browser.switch_to_default_content()
                browser.switch_to_frame('main')
                selectTimeFrom = Select(browser.find_element_by_name('DropDownListTIME_FROM'))
                selectTimeFrom.select_by_visible_text(qop[2])
                selectTimeTo = Select(browser.find_element_by_name('DropDownListTIME_TO'))
                selectTimeTo.select_by_visible_text(qop[3])
                # time.sleep(int(delaytime))
                browser.find_element_by_id('btnAddLine').click()  #添加明细
                time.sleep(3)  #延时，防止提交按钮丢失
                browser.find_element_by_id('btnPost').click()  #提交
                print('%s号加班申请完成...' % (qop[0]))
                # browser.find_element_by_id('btnCancel').click()  #取消申请

    #退出浏览器
    browser.quit()


if __name__ == '__main__':
    commandLineInterface()
