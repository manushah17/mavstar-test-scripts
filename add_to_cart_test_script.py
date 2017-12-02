import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://mavstaruno.pythonanywhere.com/login/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       assert "Logged In"
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       #driver.get('http://mavstaruno.pythonanywhere.com/')
       time.sleep(3)
       #elem = driver.find_elements_by_xpath('//*[@id="app-layout"]/div[2]/div/div/div/div/div[4]/div/div/a')
       #driver.get('http://mavstaruno.pythonanywhere.com/13/baseball-gear/')
       driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/div/div/div/div/div[4]/div/a').click()

       time.sleep(3)
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/div/div/div[2]/div/form').click()
       #time.sleep(5)
      # driver.get('http://mavstaruno.pythonanywhere.com/cart/')
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]')
       time.sleep(1)

   def tearDown(self):
       self.driver.close()


if __name__ == "__main__":
   unittest.main()



