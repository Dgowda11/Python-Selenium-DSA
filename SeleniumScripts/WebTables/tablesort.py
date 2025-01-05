import time
from sys import executable
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
chrome_options.add_argument("--executable_path=drivers\\chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
browserSortedList  = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# Get the list of all webElements
veggieList = driver.find_elements(By.XPATH,"//tr/td[1]")

# Append all the elements into the list
for veg in veggieList:
    browserSortedList.append(veg.text)

# make the copy of the list before comparing
orginalBorwserList  = browserSortedList.copy()

# Perfom the sorting on the list
browserSortedList.sort()

print(orginalBorwserList)
print(browserSortedList)
assert browserSortedList == orginalBorwserList