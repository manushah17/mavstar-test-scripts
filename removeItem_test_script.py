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
        time.sleep(3)

        id_quantity = 5
        #select item; bag pack
        elem = driver.find_element_by_xpath(("/html/body/div[2]/div/div/div/div/div[1]/div/a/img")).click()
        time.sleep(3)
        #Add item to cart
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/input[3]").click()
        time.sleep(3)
        # click on continue shopping to add more item to cart by taking the user back to homepage
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/a[1]")
        time.sleep(3)
        driver.get("http://mavstaruno.pythonanywhere.com/")
        time.sleep(3)
        #Add another product; baseball gear
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[4]/div/div/a").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/input[3]").click()
        time.sleep(3)
        # click on continue shopping to add more item to cart by taking the user back to homepage
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/a[1]")
        time.sleep(3)
        #Add item from the apparels department to cart
        driver.get("http://mavstaruno.pythonanywhere.com/apparel-uniforms/")
        time.sleep(3)
        #Select item; jersey
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/div/a/img").click()
        time.sleep(2)
        # Add jersey to cart
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/input[3]").click()
        time.sleep(3)
        #To remove an an item from the cart; back pack
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/table/tbody/tr[2]/td[4]/a").click()
        time.sleep(3)
        # click on continue shopping to add more item to cart by taking the user back to homepage
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/a[1]")
        time.sleep(3)
        #To continue shopping
        # Add another item to cart from the ball department
        driver.get("http://mavstaruno.pythonanywhere.com/balls/")
        time.sleep(3)
        # Select item; football
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/div/div/a").click()
        time.sleep(3)
        # Add football to cart
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/input[3]").click()
        time.sleep(3)
        driver.get("http://mavstaruno.pythonanywhere.com/")
        time.sleep(1)
        # The tearDown function quits the driver
    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main()        
