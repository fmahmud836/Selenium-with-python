from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

#count how many textbox in the website
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
inputBox = driver.find_elements(By.CLASS_NAME, "text_field")
print(len(inputBox))

print(driver.find_element(By.ID,"RESULT_TextField-1").is_displayed())

#how to provide value in text boxes
driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Fahim")
driver.find_element(By.ID,"RESULT_TextField-2").send_keys("Mahmud")