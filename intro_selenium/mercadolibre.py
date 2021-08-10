from selenium import webdriver
import unittest
from time import sleep

class TestingMercadoLibre(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = self.driver
        driver.get('https://www.mercadolibre.com/')
        driver.maximize_window()

    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        location = driver.find_element_by_partial_link_text('Bogotá D.C.')
        location.click()
        sleep(3)

        condition = driver.find_element_by_partial_link_text('Nueva')
        condition.click()
        sleep(3)

        order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        higher_price = driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div > div.ui-search-sort-filter > div > div > div > ul > li:nth-child(3) > a > div > div')
        higher_price.click()
        sleep(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[2]/a/h2')
            articles.append(article_name.text)

            article_price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[3]/div[1]/div[1]/a/div/div/span[1]/span[2]/span[2]')
            prices.append(article_price.text)

        print(articles,prices)
            


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    