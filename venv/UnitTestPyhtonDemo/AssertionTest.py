import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com/")
        title_of_webpage = driver.title
        #assertEqual
        #self.assertEqual("Google", title_of_webpage, "Webpage title is  same")

        #assertNotEqual
        self.assertNotEqual("Google1", title_of_webpage, "Webpage title is not same")

if  __name__ == "__main__":
    unittest.main()