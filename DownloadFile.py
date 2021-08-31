from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
chromeOptions.add_experimental_option("pref",{'download.default_directory' : 'C:\Users\Fahim Mahmud\PycharmProjects\SeleniumProject\default_download'})
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe", chrome_options= chromeOptions)


driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()
driver.find_element_by_xpath('//*[@id="textbox"]').send_keys("Send keys")
driver.find_element_by_xpath('//*[@id="createTxt"]').click()
driver.find_element_by_xpath('//*[@id="link-to-download"]').click()
