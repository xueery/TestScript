from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("易烊千玺")
driver.find_element_by_id("su").click()
time.sleep(6)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(6)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'c')
time.sleep(6)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(6)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
time.sleep(6)
driver.quit()
