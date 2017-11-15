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
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)

        id_quantity = 5
        #select item; bag pack
        elem = driver.find_element_by_xpath(("/html/body/div[2]/div/div/div/div/div[1]/div/a/img")).click()
        time.sleep(5)
        #Add item to cart
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/input[3]").click()
        time.sleep(5)
        # click on continue shopping to add more item to cart by taking the user back to homepage
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/a[1]")
        time.sleep(5)
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)
        #Add another product; baseball gear
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[4]/div/div/a").click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/input[3]").click()
        time.sleep(5)
        # click on continue shopping to add more item to cart by taking the user back to homepage
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/a[1]")
        time.sleep(5)
        #Add item from the apparels department to cart
        driver.get("http://127.0.0.1:8000/apparel-uniforms/")
        time.sleep(5)
        #Select item; jersey
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/div/a/img").click()
        time.sleep(5)
        # Add jersey to cart
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/input[3]").click()
        time.sleep(5)
        #To remove an an item from the cart; back pack
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/table/tbody/tr[2]/td[4]/a").click()
        time.sleep(5)
        # click on continue shopping to add more item to cart by taking the user back to homepage
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/a[1]")
        time.sleep(5)
        #To continue shopping
        # Add another item to cart from the ball department
        driver.get("http://127.0.0.1:8000/balls/")
        time.sleep(5)
        # Select item; football
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/div/div/a").click()
        time.sleep(5)
        # Add football to cart
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/input[3]").click()
        time.sleep(5)
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)
        # The tearDown function quits the driver
    def tearDown(self):
        self.driver.close()
