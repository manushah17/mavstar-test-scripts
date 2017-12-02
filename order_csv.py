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
class Order_csv(unittest.TestCase):   

    @classmethod
    def setUp(self):
       self.driver = webdriver.Chrome()
       self.driver.maximize_window()

    def test_order_csv(self):
       
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
       
       div_checkbox = driver.find_element_by_id("action-toggle").click()
       time.sleep(3)
       id_action = 'Export to CSV'
       select = Select(driver.find_element_by_name('action'))
       select.select_by_visible_text(id_action)
       
       
       btn_go = driver.find_element_by_xpath('//*[@id="changelist-form"]/div[1]/button').click()
       time.sleep(3)
       
              
    def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
