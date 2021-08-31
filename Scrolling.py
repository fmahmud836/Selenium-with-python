from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window() #maximize the window size

# Scroll down by pixel
#driver.execute_script("window.scrollBy(0,1000)","")

# Scroll down till the element is visible
flag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[66]/td[2]')
driver.execute_script("arguments[0].scrollIntoView();", flag)

# Scroll down till the end

driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

