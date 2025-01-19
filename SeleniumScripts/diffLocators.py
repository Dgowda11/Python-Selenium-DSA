import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print("Title",driver.title,"URL", driver.current_url)

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Darshan")
driver.find_element(By.NAME,'email').send_keys("Darshan@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Qwerty@123")
driver.find_element(By.ID,"exampleCheck1").click()

# Handle Static Drop down
dropDown = Select(driver.find_element(By.XPATH,"//label[text()='Gender']/following-sibling::select"))
dropDown.select_by_visible_text("Male")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
# Check the print the success message
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("DarshanGowda")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()

time.sleep(2)