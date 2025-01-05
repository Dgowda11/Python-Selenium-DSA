import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR,".blinkingText:nth-child(1)").click()
childWindows = driver.window_handles
driver.switch_to.window(childWindows[1])
mailID  = driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text
driver.switch_to.window(childWindows[0])

# Use that MailID to login
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(mailID)
driver.find_element(By.ID,"password").send_keys("Qwerty@1234")
driver.find_element(By.ID,"signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//form[@id='login-form']/div/strong")))
print(driver.find_element(By.XPATH,"//form[@id='login-form']/div/strong").text)
time.sleep(2)