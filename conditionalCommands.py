from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")

user_email = driver.find_element_by_xpath('//*[@id="eid"]/input')
user_email.send_keys("fmahmud836@gmail.com")

radio_male = driver.find_element_by_css_selector('#basicBootstrapForm > div:nth-child(5) > div > label:nth-child(1) > input')
radio_female = driver.find_element_by_css_selector('#basicBootstrapForm > div:nth-child(5) > div > label:nth-child(2) > input')
print("Male ",radio_male.is_selected())
print("Female: ", radio_female.is_selected())

radio_male.click()
print("Male ",radio_male.is_selected())
radio_female.click()
print("Female ", radio_female.is_selected())
driver.close()