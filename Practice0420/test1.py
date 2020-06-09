from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
driver.get("http://news.baidu.com")
q =driver.find_element_by_xpath(".//*[@id='s_btn_wr']")
# 右键
# 行为事件是存储在actionchains对象队列,使用perform()，事件按顺序执行。
ActionChains(driver).context_click(q).perform()
# 双击
ActionChains(driver).double_click(q).perform()
time.sleep(8)
driver.quit()