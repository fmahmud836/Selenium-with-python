from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.switch_to_frame(0)

driver.find_element_by_id('id="RESULT_FileUpload-10"').send_keys("C:\Users\Fahim Mahmud\PycharmProjects\SeleniumProject\data\Fahim.txt")