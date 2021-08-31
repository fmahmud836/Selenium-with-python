from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("http://newtours.demoaut.com")

#Number of links
links = driver.find_elements_by_tag_name("a")
print("Number of links: ", len(links))

#print links
for link in links:
    print(link.text)

#clicking on links
#driver.find_element(By.LINK_TEXT, "Privacy Policy").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Pri").click()

