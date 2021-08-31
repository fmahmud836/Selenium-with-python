from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
element = driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button')
element.click()


#Actions on alert button
#driver.switch_to_alert().accept() #closes alert window with OK button
driver.switch_to_alert().dismiss() #closes alert with Cancel button