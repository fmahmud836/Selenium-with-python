import unittest


class PaymentTest(unittest.TestCase):
    def test_PaymentInDollar(self):
        print("This is payment in dollar test")
        self.assertTrue(True)

    def testPaymentInRupees(self):
        print("This is payment in Rupees")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main
