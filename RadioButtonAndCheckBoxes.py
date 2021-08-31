from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")



radio_button_male = driver.find_element(By.CSS_SELECTOR,"#q26 > table > tbody > tr:nth-child(1) > td > label")
radio_button_female = driver.find_element(By.CSS_SELECTOR,"#q26 > table > tbody > tr:nth-child(2) > td > label")

#working with radio buttons
radio_button_male_status = radio_button_male.is_selected()
radio_button_female_status = radio_button_female.is_selected()

print(radio_button_male_status)
print(radio_button_female_status)

driver.find_element(By.CSS_SELECTOR, "#q26 > table > tbody > tr:nth-child(1) > td > label").click() #select the radiobutton
radio_button_male = driver.find_element(By.ID, "RESULT_RadioButton-7_0").is_selected() #status should be true
print("status of the radio button male", radio_button_male)  #print true status


#wprking with checkboxes

option1 = driver.find_element(By.ID,"RESULT_CheckBox-8_0")
print(option1.is_selected())

driver.find_element(By.CSS_SELECTOR,"#q15 > table > tbody > tr:nth-child(1) > td > label").click()
print("Sunday: ",option1.is_selected())

