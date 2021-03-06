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

        id_quantity = 8
        #select item; bag pack, with a quantity of 8
        elem = driver.find_element_by_xpath(("/html/body/div[2]/div/div/div/div/div[1]/div/a/img")).click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys(id_quantity)
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/input[3]").click()
        time.sleep(2)
        # click on continue shopping to add more item to cart by taking the user back to homepage
        driver.find_element_by_xpath('//*[@id="app-layout"]/div[2]/div/div[3]/a[1]').click()
       # driver.get("http://mavstaruno.pythonanywhere.com/")
        time.sleep(3)
        # Add another product; baseball gear
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[4]/div/div/a").click()
        time.sleep(3)
        id_quantity = 3
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys(id_quantity)
        time.sleep(3)
        #Add item to cart
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/input[3]").click()
        time.sleep(3)
        # To update the quantity of the back pack to 5, and automatically show the updated price
        id_quantity = 5
        #Finds the id_quantity and assigns the quantity to 5
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys(id_quantity)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/table/tbody/tr[1]/td[3]/form/input[2]").click()
        time.sleep(3)
        # click on continue shopping to add more item to cart by taking the user back to homepage
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/a[1]").click()
        time.sleep(2)
        driver.get("http://mavstaruno.pythonanywhere.com/")
        time.sleep(1)
        # The tearDown function quits the driver
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()        
