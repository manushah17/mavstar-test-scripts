import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test_Logout(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome('/Users/srishtynayak/Downloads/mavstar-sporting-goods-master 5\chromedriver')

   def test_blog(self):
       id_username= "Srishty13"
       id_password= "qwerty123456"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://mavstaruno.pythonanywhere.com")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(id_username)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(id_password)
       elem.send_keys(Keys.RETURN)
       driver.get("http://mavstaruno.pythonanywhere.com/Login")
       elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[2]/a').click()
       assert "Logged In"
       time.sleep(5)
       driver.get("http://mavstaruno.pythonanywhere.com/apparel-uniforms/")
       elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[2]/a').click()
       assert "Logout"
       time.sleep(5)

   def tearDown(self):
       self.driver.close()
