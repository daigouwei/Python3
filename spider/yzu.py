#!/usr/bin/env
#-*- coding:utf-8 -*-

# import time
import requests
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

username = input('请输入用户名：')
password = input('请输入密码：')
url = 'http://yjsglxt.yzu.edu.cn/pyxx/login.aspx'
broswer = webdriver.PhantomJS()
broswer.set_window_size(900, 900)#不能跟Chrome一样全屏，原因未知。

# 使用Chrome截图会是黑色图，可以全屏，原因未知。
# broswer = webdriver.Chrome()
# broswer.maximize_window()

broswer.get(url)

# time.sleep(10)
# broswer.implicitly_wait(30)

broswer.save_screenshot('yzm.png')
elemUsername = broswer.find_element_by_name('ctl00$txtusername')
elemUsername.send_keys(username)
elemPassword = broswer.find_element_by_name('ctl00$txtpassword')
elemPassword.send_keys(password)
elemYzm = broswer.find_element_by_name('ctl00$txtyzm')

# 由于yzu的验证码是纯动态的，就算拿到具体时间的验证码网址，会发现两次访问同一个网址验证码也是不一样的，所以注释方法不行。
# yzmLink = broswer.find_element_by_id('myCode').get_attribute('src')
# yzmRe = requests.get(yzmLink)
# gifData = yzmRe.content.split(b'\r\n', 1)
# with open('yzm.gif', 'wb') as f:
    # f.write(gifData[0])

yzm = input('请打开验证码图yzm.png，输入验证码：')
elemYzm.send_keys(yzm)
elemAccount = broswer.find_element_by_name('ctl00$ImageButton1')
elemAccount.click()
# print(broswer.page_source)
broswer.switch_to_frame('PageFrame')#有深层frame需要切换frame抓取
# print(broswer.page_source)
photoUrl = broswer.find_element_by_id('imgPhoto').get_attribute('src')
photoRe = requests.get(photoUrl)
photoData = photoRe.content
with open('photo.jpg', 'wb') as f:
    f.write(photoData)

broswer.quit()


