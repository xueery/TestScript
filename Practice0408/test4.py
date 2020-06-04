from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
# 设置窗口最大化
driver.maximize_window()
driver.find_element_by_link_text("新闻").click()
time.sleep(6)
# 这个语句出错
#print(driver.title)
# 后退
driver.back()
time.sleep(6)
#print(driver.title)
# 前进
driver.forward()
# 设置固定的窗口大小
driver.set_window_size(500,800)
time.sleep(6)
#print(driver.title)
time.sleep(8)
driver.quit()