import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"  # instructor
        pwd = "instructor1a"  # instructor1a
        driver = self.driver
        driver.maximize_window()
        driver.get("http://mavstaruno.pythonanywhere.com/login")
        # driver.get("http://127.0.0.1:8000/login")
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/div/div/div/div/div[1]/div/a').click()
        time.sleep(3)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/div/div/div[2]/div/form/input[3]').click()
        time.sleep(3)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/div/div[3]/a[2]').click()
        time.sleep(1)


    def tearDown(self):
         self.driver.close()


if __name__ == "__main__":
    unittest.main()