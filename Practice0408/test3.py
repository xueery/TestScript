from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")

#获取 html 文件的 head
title=driver.title
print(title)
# 获取请求的 url
url=driver.current_url
print(url)
# driver.find_element_by_id("kw").send_keys("易烊千玺")
# driver.find_element_by_id("su").click()
# # 智能等待
# driver.implicitly_wait(10)
# driver.find_element_by_link_text("易烊千玺_百度百科").click()
time.sleep(8)
driver.quit()