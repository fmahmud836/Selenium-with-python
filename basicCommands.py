from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")


driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

print(driver.title) #title of the page
print(driver.current_url) #url of the page


time.sleep(8)

driver.close() # close parent site
driver.quit() # close all
