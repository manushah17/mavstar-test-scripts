import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       id_username= "instructor"
       id_password= "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://mavstaruno.pythonanywhere.com")
       time.sleep(2)
       driver.get("http://mavstaruno.pythonanywhere.com/login/")
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(id_username)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(id_password)
       elem.send_keys(Keys.RETURN)
       time.sleep(2)
       assert "Logged In"
       time.sleep(3)
       driver.get("http://mavstaruno.pythonanywhere.com/apparel-uniforms/")
       elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[2]/a').click()
       assert "Logout"
       time.sleep(1)

   def tearDown(self):
       self.driver.close()
       


if __name__ == "__main__":
    unittest.main()