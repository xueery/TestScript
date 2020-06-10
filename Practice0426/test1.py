# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import os
# 操作alert框
dr = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('./htmlDirectory/alert.html')
dr.get(file_path)
print(file_path)
# 点击链接弹出alert
dr.find_element_by_id('tooltip').click()
sleep(2)
# 获取到弹出的alert
alert = dr.switch_to.alert
alert.accept()
sleep(2)
dr.quit()