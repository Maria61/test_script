from selenium import webdriver
import time
import os
from selenium.webdriver.common.action_chains import ActionChains


# 层级定位：点击按钮后，出现多个按钮可以选择，点击并进行相应的跳转或弹出处理

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('level_locate.html')
driver.get(file_path)
time.sleep(6)
# 先定位到触发下拉框选项的元素并点击
driver.find_element_by_link_text("Link1").click()
time.sleep(10)
# WebDriverWait(dr,10).until(lambda the_driver:the_driver.find_element_by_id('dropdown1').is_display()) #每隔500ms扫描一次的等待
# 先定位到ul，然后定位到具体的要点击的li元素
list = driver.find_element_by_id("dropdown1").find_elements_by_link_text("Action") # Action只有一个，这里的list是？
driver.implicitly_wait(10)
# 通过动作事件中的 move... 移动鼠标，perform选中元素
ActionChains(driver).move_to_element(list[0]).perform()
time.sleep(4)
driver.quit()

