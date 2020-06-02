from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")

# driver.find_element_by_id("kw").send_keys("TFBOYS")
# driver.find_element_by_id("su").submit()
# time.sleep(8)
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("白敬亭")
# driver.find_element_by_id("su").submit()
data=driver.find_element_by_id("s-bottom-layer-right").text
print(data)
time.sleep(8)
driver.quit()