import unittest
from SeleniumPythonRefactorTestCase import Test_login
from SeleniumPythonMultipleTests import Test_Forgot_Pwd

# get all tests from SearchText and HomePageTest class
login_test = unittest.TestLoader().loadTestsFromTestCase(Test_login)
forgot_pwd_test = unittest.TestLoader().loadTestsFromTestCase(Test_Forgot_Pwd)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([login_test, forgot_pwd_test])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)