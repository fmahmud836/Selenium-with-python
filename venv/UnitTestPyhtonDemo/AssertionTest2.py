import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com/")
        title_of_webpage = driver.title
        #assertTrue
        #self.assertTrue(title_of_webpage == "Google")
        #assertFalse
        self.assertFalse(title_of_webpage == "Google")


if  __name__ == "__main__":
    unittest.main()