import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
addTochart = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(addTochart)
assert count > 0
# We can't use the Implicit for interacting with List we need to use Dead Wait
time.sleep(3)
for chart in addTochart:
    chart.find_element(By.XPATH,"div/button").click()

#Click on the Cart
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
promoCode = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
time.sleep(3)