from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")

# driver.find_element_by_id("kw").send_keys("易烊千玺")
# driver.find_element_by_name("wd").send_keys("易烊千玺")
# time.sleep(6)
# driver.find_element_by_id("su").click()
# driver.find_element_by_class_name("s_ipt").send_keys("王源")
# time.sleep(6)
# # 不能根据 class_name进行搜索
# driver.find_element_by_class_name("bg s_btn").click()
# 根据链接文本来搜索
# driver.find_element_by_link_text("抗击肺炎").click()
# 根据部分链接文本来搜索
# driver.find_element_by_partial_link_text("肺炎").click()
# driver.find_element_by_xpath("//*[@name='wd']").send_keys("易烊千玺")
# driver.find_element_by_xpath("//*[@id='su']").click()
driver.find_element_by_css_selector("#kw").send_keys("白敬亭")
driver.find_element_by_css_selector("#su").click()
time.sleep(8)
driver.quit()