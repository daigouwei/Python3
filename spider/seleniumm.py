#!/usr/bin/env
# -*- coding:utf-8 -*-

'''1
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
'''

'''2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.python.org')
assert 'Python' in driver.title
elem = driver.find_element_by_name('q')
elem.send_keys('pycon')
elem.send_keys(Keys.ENTER)
print(driver.page_source)
'''

# '''3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://somedomain/url_that_delays_loading')
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'myDynamicElement'))
    )
finally:
    driver.quit()
