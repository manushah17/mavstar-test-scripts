import unittest
import Test_login, Search_Product 
import Browse_test_script, add_to_cart_test_script
import updateQuantity_test_script,removeItem_test_script
import checkout,place_order,logout
import Test_Forgot_Pwd,register
import order_pdf,order_csv, view_order_details    
    

class ConfigTestCase(unittest.TestCase):
    
    def setUp(self):
        print('set up')

    def runTest(self):
        print('run test')

def suite():
    
    test_suite = unittest.TestSuite()
   
    test_suite.addTest(unittest.loader.findTestCases(Test_login))
    test_suite.addTest(unittest.loader.findTestCases(Search_Product))
    test_suite.addTest(unittest.loader.findTestCases(Browse_test_script))
    test_suite.addTest(unittest.loader.findTestCases(add_to_cart_test_script))
    test_suite.addTest(unittest.loader.findTestCases(updateQuantity_test_script))
    test_suite.addTest(unittest.loader.findTestCases(removeItem_test_script))
    test_suite.addTest(unittest.loader.findTestCases(checkout))
    test_suite.addTest(unittest.loader.findTestCases(place_order))
    test_suite.addTest(unittest.loader.findTestCases(logout))
    test_suite.addTest(unittest.loader.findTestCases(Test_Forgot_Pwd))
    test_suite.addTest(unittest.loader.findTestCases(register))
    test_suite.addTest(unittest.loader.findTestCases(view_order_details))
    test_suite.addTest(unittest.loader.findTestCases(order_csv))
    test_suite.addTest(unittest.loader.findTestCases(order_pdf))  
    
    return test_suite

mySuit=suite()


runner=unittest.TextTestRunner()
runner.run(mySuit)