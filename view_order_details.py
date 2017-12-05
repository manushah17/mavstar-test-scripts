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
class View_Order_Details(unittest.TestCase):   

    @classmethod
    def setUp(self):
       self.driver = webdriver.Chrome()
       self.driver.maximize_window()

    def test_view_order(self):
       
       user = "instructor" # instructor
       pwd = "instructor1a" #instructor1a
       driver = self.driver
       driver.get("http://mavstaruno.pythonanywhere.com/admin")
       #driver.get("http://127.0.0.1:8000/admin")
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       time.sleep(1)
       
       div_order = driver.find_element_by_xpath('//*[@id="content-main"]/div[3]/table/tbody/tr/th/a').click()
       time.sleep(3)
       
       view_link = driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[1]/td[11]/a').click()
       time.sleep(3)
       
       driver.find_element_by_xpath('//*[@id="container"]/div[2]/a[2]').click()
       time.sleep(3)
       
       driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[8]/td[11]/a').click()
       time.sleep(3)
       
              
    def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
