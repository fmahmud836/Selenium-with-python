import unittest


class SignUpTest(unittest.TestCase):
    def test_signUpByEmail(self):
        print("This is signUp by email test")
        self.assertTrue(True)

    def test_signUpByFacebook(self):
        print("This is signUp by Facebook test")
        self.assertTrue(True)

    def test_signUpByTwitter(self):
        print("This is signup by Twitter Page")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
