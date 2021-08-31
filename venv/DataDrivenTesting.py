import ExcelUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("https://www.busuu.com/en/login")
driver.maximize_window()

path = r"C:\Users\Fahim Mahmud\PycharmProjects\SeleniumProject\data\DemoCredntial_DataDrivenTesting.xlsx"
rows = ExcelUtils.getRowCount(path, "Sheet1")

for r in range(2, rows+1):
    userName = ExcelUtils.readData(path,"Sheet1",r,1)
    passWord = ExcelUtils.readData(path,"Sheet1",r,2)
    driver.find_element_by_xpath('//*[@id="login-form-field-switch"]/div[1]/input').send_keys(userName)
    driver.find_element_by_xpath('//*[@id="login-form-password"]').send_keys(passWord)
    driver.find_element_by_xpath('//*[@id="login-form-submit"]').click()






