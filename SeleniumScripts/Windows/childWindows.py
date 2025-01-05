import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(2)
# First Window
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowOpend = driver.window_handles
driver.switch_to.window(windowOpend[1])
time.sleep(2)
driver.switch_to.window(windowOpend[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text
time.sleep(2)