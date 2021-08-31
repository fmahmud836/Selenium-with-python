from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("http://newtours.demoaut.com")
print(driver.title)

driver.get("http://pavantestingtools.blogspot.in/")
print(driver.title)

time.sleep(5)
driver.back()
print(driver.title)


driver.forward()
time.sleep(5)
print(driver.title)

driver.close()
