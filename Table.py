from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("file:///D:/Selenium/Table.html")


rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
col = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))



print(rows)
print(col)
