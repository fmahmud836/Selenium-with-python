import unittest

class AppTesting(unittest.TestCase):
    @unittest.SkipTest
    def test_seacrh(self):
        print("This is a search test")
    @unittest.skip("Hudai skip")
    def test_advance_search(self):
        print("This is advanced seacrh test")
    @unittest.skipIf(1 == 1, "One is One")
    def test_preparetionRecharge(self):
        print("This is a prepaid recharge test")
    def test_postpaidRecharge(self):
        print("This is a postpaid recharge")
    def test_loginByGmail(self):
        print("This is by Gmail")
    def test_loginByTwitter(self):
        print("This is by twitter")
if  __name__ == "__main__":
    unittest.main()