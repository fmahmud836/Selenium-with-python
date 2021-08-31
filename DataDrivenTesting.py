import ExcelUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("http://www.testyou.in/Login.aspx")
driver.maximize_window()

path = r"C:\Users\Fahim Mahmud\PycharmProjects\SeleniumProject\data\DemoCredntial_DataDrivenTesting.xlsx"

rows = ExcelUtils.getRowCount(path, 'Sheet1')

for r in range(2, rows + 1):
    username = ExcelUtils.readData(path, "Sheet1", r, 1)
    password = ExcelUtils.readData(path, "Sheet1", r, 2)
    textUser = driver.find_element_by_xpath('//*[@id="ctl00_CPHContainer_txtUserLogin"]')
    textPassword = driver.find_element_by_xpath('//*[@id="ctl00_CPHContainer_txtPassword"]')

    textUser.send_keys(username)
    textPassword.send_keys(password)

    driver.find_element_by_xpath('//*[@id="ctl00_CPHContainer_btnLoginn"]').click()
    if driver.title == "Student Dashboard | Test Maker - TestYou":
        print("test is passed")
        ExcelUtils.writeData(path, "Sheet1", r, 3, "Test Passed")
        driver.find_element_by_xpath('//*[@id="ctl00_headerTopStudent_lnkbtnSignout"]').click()
    else:
        print("test is failed")
        ExcelUtils.writeData(path, "Sheet1", r, 3, "Test Failed")
        driver.get("http://www.testyou.in/Login.aspx")
