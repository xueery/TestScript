from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")

driver.find_element_by_name("wd").send_keys("易烊千玺")
driver.find_element_by_id("su").click()
driver.set_window_size(400,800)
time.sleep(6)
#让浏览器滑到最低端
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(8)
#让浏览器滑到最顶端
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(8)
driver.quit()