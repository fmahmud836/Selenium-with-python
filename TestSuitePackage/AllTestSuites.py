import unittest
from Package1.TC_loginTest import LogInTest
from Package1.TC_SignUpTest import SignUpTest
from Package2.Test_PaymentReturn import PaymentReturnsTest
from Package2.TC_PayemntTest import PaymentTest

# Get all test method from LogInTest,SignUpTest,PaymentReturnsTest,PaymentTest
tc1 = unittest.TestLoader().loadTestsFromTestCase(LogInTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Create test suites
sanityTestSuite = unittest.TestSuite([tc1, tc2])
functionalTestSuite = unittest.TestSuite([tc3, tc4])
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])

unittest.TextTestRunner().run(masterTestSuite)
