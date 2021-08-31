from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("http://www.testyou.in/Login.aspx")
driver.maximize_window()

#driver.save_screenshot(r"C:\Users\Fahim Mahmud\PycharmProjects\SeleniumProject\data\screenshooot1.png")
driver.get_screenshot_as_file(r"C:\Users\Fahim Mahmud\PycharmProjects\SeleniumProject\data\screenshooot1.jpg")
