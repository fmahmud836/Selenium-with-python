from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com/")

driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div[1]/div[5]/div/div/div/div/div/ul/li[2]/a').click()
driver.find_element(By.NAME, 'Leaving from').click()