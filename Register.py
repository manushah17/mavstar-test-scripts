import  unittest

import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

class Test_register(unittest.TestCase):



   def setUp(self):

       self.driver = webdriver.Chrome('/Users/srishtynayak/Downloads/mavstar-sporting-goods-master 5\chromedriver')

   def test_blog(self):

       id_username = "srishty"

       id_email = "srishtynayak@gmail.com"

       id_password = "qwert12345"

       driver = self.driver

       driver.maximize_window()

       driver.get("http://mavstaruno.pythonanywhere.com")

       elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/li[2]/a').click()

       time.sleep(5)

       elem.send_keys(Keys.RETURN)

       driver.get("http://mavstaruno.pythonanywhere.com")

       assert "Register"

       elem = driver.find_element_by_id("id_username")

       elem.send_keys(id_username)

       elem = driver.find_element_by_id("id_email")

       elem.send_keys(id_email)

       elem = driver.find_element_by_id("id_password")

       elem.send_keys(id_password)

       elem = driver.find_element_by_id("id_email2")

       elem.send_keys(id_email)

       time.sleep(5)

       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/form/div/input[2]').click()

       time.sleep(5)



   def tearDown(self):

       self.driver.close()
