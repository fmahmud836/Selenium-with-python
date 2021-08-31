import unittest
from selenium import webdriver
def setUpModule():
    print("Set up module")
def tearDownModule():
    print("Tear Down Module")
class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("This is login test")
    @classmethod
    def tearDown(self):
        print("This is a logout test")
    @classmethod
    def setUpClass(cls):
        print("Application open")
    @classmethod
    def tearDownClass(cls):
        print("Closed")
    def test_seacrh(self):
        print("This is a search test")
    def test_advance_search(self):
        print("This is advanced seacrh test")
    def test_preparetionRecharge(self):
        print("Thisis a prepaid recharge test")
    def test_postpaidRecharge(self):
        print("This is a postpaid recharge")

if __name__ == '__main__':
    unittest.main()
