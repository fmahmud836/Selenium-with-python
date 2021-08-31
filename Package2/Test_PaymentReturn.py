import unittest


class PaymentReturnsTest(unittest.TestCase):
    def test_PaymentReturnsInDollar(self):
        print("This is payment return in dollar test")
        self.assertTrue(True)

    def testPaymentReturnsInRupees(self):
        print("This is payment return in Rupees")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main
