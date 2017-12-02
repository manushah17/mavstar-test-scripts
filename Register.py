import unittest

import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       id_username = "mav_guest"
       id_email = "mav_guest@gmail.com"
       id_password = "guest123$"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://mavstaruno.pythonanywhere.com")
       elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[3]/a').click()
       time.sleep(3)
       assert "Register"
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(id_username)
       elem = driver.find_element_by_id("id_email")
       elem.send_keys(id_email)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(id_password)
       elem = driver.find_element_by_id("id_email2")
       elem.send_keys(id_email)
       time.sleep(3)
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/form/div/input[2]').click()
       time.sleep(2)



   def tearDown(self):
       self.driver.close()
       
       
if __name__ == "__main__":
    unittest.main()