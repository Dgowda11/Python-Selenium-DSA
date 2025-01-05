import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
print("Title",driver.title,"URL", driver.current_url)
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("Qwerty@1234")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(3) input").send_keys("Qwerty@1234")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

print("Title",driver.title,"URL", driver.current_url)
time.sleep(5)