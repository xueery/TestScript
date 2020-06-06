from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get("http://127.0.0.1:88/biz/user-login-L2Jpei8=.html")

driver.maximize_window()
driver.find_element_by_id("account").clear()
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_id("account").send_keys(Keys.TAB)
time.sleep(6)
driver.find_element_by_name("password").send_keys("123456")
time.sleep(3)
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(8)
driver.quit()
