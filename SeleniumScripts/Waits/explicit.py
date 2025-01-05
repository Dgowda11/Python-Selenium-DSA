import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
orginalList = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actualitems = []

addTochart = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(addTochart)
assert count > 0
time.sleep(4)
for chart in addTochart:
    actualitems.append(chart.find_element(By.XPATH,"h4").text)
    chart.find_element(By.XPATH,"div/button").click()

assert  orginalList == actualitems

# Click on the Cart
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait  = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
totalamt = driver.find_element(By.XPATH,"//span[@class='totAmt']").text
amts = driver.find_elements(By.XPATH,"//tbody/tr/td[5]")

sum = 0
for amt in amts:
    sum = sum + int(amt.text)

assert sum == int(totalamt)
print()
# Check is after Discount is less than Gross amount
discountamt = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(discountamt)
assert  int(totalamt) > discountamt
time.sleep(3)