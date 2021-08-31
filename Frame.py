from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("packageListFrame") #First Frame
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(4)
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame") #Second Frame
driver.find_element_by_link_text("TakesScreenshot").click()
time.sleep(4)
driver.switch_to.default_content()

driver.switch_to.frame("classFrame") #Third frame
driver.find_element_by_xpath("/html/body/header/nav/div[1]/div[1]/ul/li[6]/a").click()
time.sleep(4)
driver.switch_to.default_content()