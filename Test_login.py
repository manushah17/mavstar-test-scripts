import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime

#
class Test_login(unittest.TestCase):   

    @classmethod
    def setUp(self):
       self.driver = webdriver.Chrome()
       self.driver.maximize_window()

    def test_user_login(self):
       
       user = "instructor" # instructor
       pwd = "instructor1a" #instructor1a
       driver = self.driver
       driver.get("http://mavstaruno.pythonanywhere.com/login")
       #driver.get("http://127.0.0.1:8000/login")
       time.sleep(5)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(3)
       elem.send_keys(Keys.RETURN)
       time.sleep(3)
       
       # mouse over on non-stock investment image and View Details button
       invApp_uniform = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[1]/li[2]/a').click()
       time.sleep(3)
       invApp_uniform_product = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/div/div/div/div/div[2]/div/a/img').click()
       time.sleep(5)
       
       invApp_uniform = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/div/div/div[2]/div/form/input[3]').click()
       time.sleep(3)
       invBats = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[1]/li[5]/a').click()
       time.sleep(3)
       invBats = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[2]/a').click()
       time.sleep(3)

       
    @classmethod
    def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
