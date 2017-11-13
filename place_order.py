import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\python4900\chromedriver.exe')

    def test_blog(self):
        user = "superadmin"  # instructor
        pwd = "admin123"  # instructor1a
        id_first_name = "karthik"
        id_last_name = "bellary"
        id_email = "abcasdasd@gmail.com"
        id_address = "crosswinds"
        id_postal_code = "68106"
        id_city = "Omaha"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://mavstaruno.pythonanywhere.com/login")
        # driver.get("http://127.0.0.1:8000/login")
        time.sleep(5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/div/div/div/div/div[1]/div/a').click()
        time.sleep(3)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/div/div/div[2]/div/form/input[3]').click()
        time.sleep(3)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/div/div[3]/a[2]').click()
        time.sleep(3)
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys(id_first_name)
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys(id_last_name)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(id_email)
        elem = driver.find_element_by_id("id_address")
        elem.send_keys(id_address)
        elem = driver.find_element_by_id("id_postal_code")
        elem.send_keys(id_postal_code)
        elem = driver.find_element_by_id("id_city")
        elem.send_keys(id_city)
        time.sleep(3)
        elem = driver.find_element_by_xpath('// *[ @ id = "content"] / form / p[7] / input').click()
        time.sleep(3)



    def tearDown(self):
         self.driver.close()


if __name__ == "__main__":
    unittest.main()