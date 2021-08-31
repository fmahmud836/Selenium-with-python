from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element_by_id("RESULT_RadioButton-9")
dropdown = Select(element)

#select by visible text
dropdown.select_by_visible_text("Evening")

#select by Index
dropdown.select_by_index(2)

#Select by value
dropdown.select_by_value("Radio-0")

#Count the number of otions
print("Length of option: ", len(dropdown.options))

#Capture all the options and print them as output

all_options = dropdown.options

for option in all_options:
    print(option.text)
