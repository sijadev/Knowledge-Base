import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_open_site(self):
        self.driver.maximize_window()
        self.driver.get(
            'https://duckduckgo.com/')
        self.assertTrue('DuckDuckGo — Privacy, simplified.', self.driver.title)

    def test_search(self):
        self.driver.maximize_window()
        self.driver.get(
            'https://duckduckgo.com/')
        text_field = self.driver.find_element(
            By.ID, 'search_form_input_homepage')
        text_field.send_keys('selenium')
        search_button = self.driver.find_element(
            By.ID, 'search_button_homepage')
        search_button.click()
        self.driver.implicitly_wait(2)
        webelements = self.driver.find_elements(
            By.CLASS_NAME, 'result__url__domain')

        for element in webelements:
            if element.text == 'https://www.selenium.dev':
                self.driver.implicitly_wait(5)
                element.click()
                self.driver.implicitly_wait(5)
                header = self.driver.find_element(By.TAG_NAME, 'h1')
                self.assertEqual(
                    'Selenium automates browsers. That\'s it!', header.text)
                break

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
