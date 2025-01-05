import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(4)
driver.find_element(By.XPATH,"//a[text()='Shop']").click()
products  = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    ProductName  = product.find_element(By.XPATH,"div/h4/a").text
    if ProductName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("india")
wait  = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='suggestions']/ul/li/a")))
driver.find_element(By.LINK_TEXT,"India").click()
# Click on I agree terms and conditions
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
# Click on Purchase
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//strong")))
Successmsg = driver.find_element(By.XPATH,"//strong").text
print(Successmsg)
assert "Success" in Successmsg
time.sleep(5)