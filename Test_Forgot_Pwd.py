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
class Test_Forgot_Pwd(unittest.TestCase):   

    def setUp(self):
       self.driver = webdriver.Chrome()

    def test_forgot_password(self):
       
       user = "superadmin" # instructor
       pwd = "admin" #instructor1a
       driver = self.driver
       driver.maximize_window()
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
       
       email = "stumanu15@gmail.com"
       invForgotPwdLink = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/form/div/p[3]/a').click()
       elem = driver.find_element_by_id("id_email")
       elem.send_keys(email)
       time.sleep(3)
       invSendEmail = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/form/p[2]/input').click()
       time.sleep(3)
              

    def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
