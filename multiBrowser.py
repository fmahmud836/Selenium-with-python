from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\driver\geckodriver-v0.29.1-win64\geckodriver")
driver.get("http://newtours.demoaut.com")
print(driver.title) #title of the page
print(driver.current_url) #url of the page


driver.close()
