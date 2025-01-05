import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
print("Title",driver.title,"URL", driver.current_url)

driver.find_element(By.XPATH,"//input[@placeholder='Type to Select']").send_keys("Ind")
time.sleep(2)
# Get the suggestions
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == 'India':
        country.click()
        break
# Assertions
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == 'India'

time.sleep(3)