from datetime import datetime
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


#
class Search_Product(unittest.TestCase):   

    def setUp(self):
       self.driver = webdriver.Chrome()
       self.driver.maximize_window()

    def test_search_product(self):
       
       search_product = 'bats'
       driver = self.driver
       #driver.get("http://mavstaruno.pythonanywhere.com/login")
       driver.get("http://mavstaruno.pythonanywhere.com/")
       time.sleep(3)
       
       elem = driver.find_element_by_id("search_prod")
       elem.send_keys(search_product)
       time.sleep(3)
       btnSearch = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/div/div/div/form/input[2]').click()
       time.sleep(3)
       
       search_product = 'hoody' 
       driver.execute_script("document.getElementById('search_prod').value=''")  
       time.sleep(3)    
       elem = driver.find_element_by_id("search_prod")
       elem.send_keys(search_product)
       time.sleep(3)
       btnSearch = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/div/div/div/form/input[2]').click()
       time.sleep(3)
       
       search_product = 'stop watch'    
       driver.execute_script("document.getElementById('search_prod').value=''")    
       time.sleep(3)
       elem = driver.find_element_by_id("search_prod")
       elem.send_keys(search_product)
       time.sleep(3)
       btnSearch = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/div/div/div/form/input[2]').click()
       time.sleep(1)
       

       
    def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
