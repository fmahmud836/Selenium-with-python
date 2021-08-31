import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def testName(self):

        list = {"python", "selenium", "java"}
        self.assertIn("python",list)
        self.assertNotIn("python", list)
if __name__ == "__main__":
    unittest.main()