import unittest
from selenium import webdriver

class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://google.com/')
        
    def test_compare_products_removal_alert(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field('platzi')
        search_field.submit()

        driver.back()
        driver.forward()
        driver.refresh()
        


    def tearDown(self):
        self.driver.quit()