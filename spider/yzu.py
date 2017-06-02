#!/usr/bin/env
#-*- coding:utf-8 -*-

# import time
import requests
from selenium import webdriver
import re
from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

username = input('请输入用户名：')
password = input('请输入密码：')
url = 'http://yjsglxt.yzu.edu.cn/pyxx/login.aspx'
browser = webdriver.PhantomJS()
browser.set_window_size(900, 900)#不能跟Chrome一样全屏，原因未知。

# 使用Chrome截图会是黑色图，可以全屏，原因未知。在mac上没有问题。
# browser = webdriver.Chrome()
# browser.maximize_window()

browser.get(url)

# time.sleep(10)
# browser.implicitly_wait(30)

browser.save_screenshot('yzm.png')
elemUsername = browser.find_element_by_name('ctl00$txtusername')
elemUsername.send_keys(username)
elemPassword = browser.find_element_by_name('ctl00$txtpassword')
elemPassword.send_keys(password)
elemYzm = browser.find_element_by_name('ctl00$txtyzm')

# 由于yzu的验证码是纯动态的，就算拿到具体时间的验证码网址，会发现两次访问同一个网址验证码也是不一样的，所以注释方法不行。
# yzmLink = browser.find_element_by_id('myCode').get_attribute('src')
# yzmRe = requests.get(yzmLink)
# gifData = yzmRe.content.split(b'\r\n', 1)
# with open('yzm.gif', 'wb') as f:
    # f.write(gifData[0])

yzm = input('请打开验证码图yzm.png，输入验证码：')
elemYzm.send_keys(yzm)
elemAccount = browser.find_element_by_name('ctl00$ImageButton1')
elemAccount.click()
# print(browser.page_source)
browser.switch_to_frame('PageFrame')#有深层frame需要切换frame抓取
# print(browser.page_source)
soup = BeautifulSoup(browser.page_source, 'lxml')
soupStr = soup.find_all(style='font-weight:bold;')
#对得到的soupStr进行类型转换成str，用正则表达式去除<br/>，才能再次使用BeautifulSoup进行处理
soupStrHandle = re.sub(re.compile('<br/>'),'',str(soupStr))#.strip()可加可不加
print(BeautifulSoup(soupStrHandle, 'lxml').span.string)
#下面两行用Chrome是可以直接下载图片的，在PhantomJS下没任何反应
photoUrl = browser.find_element_by_id('imgPhoto').get_attribute('src')
browser.get(photoUrl)
browser.quit()
