import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()


   def test_blog(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://mavstaruno.pythonanywhere.com/")
        time.sleep(2)
        driver.get('http://mavstaruno.pythonanywhere.com/apparel-uniforms/')
        time.sleep(2)
        driver.get('http://mavstaruno.pythonanywhere.com/bags-bats-pack/')
        time.sleep(2)
        driver.get('http://mavstaruno.pythonanywhere.com/balls/')
        time.sleep(2)
        driver.get('http://mavstaruno.pythonanywhere.com/gloves-mitts/')
        time.sleep(2)
        driver.get('http://mavstaruno.pythonanywhere.com/helmet-protective-gear/')
        time.sleep(1)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
