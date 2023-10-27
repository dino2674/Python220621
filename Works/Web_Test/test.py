import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import softest


class TestDuckDuckGo(softest.TestCase):
    def test_duckduckgo_page(self):
        CHROME_DRIVER_PATH = './chromedriver.exe'
        service = Service(executable_path=CHROME_DRIVER_PATH)
        options = webdriver.ChromeOptions()
        browser = webdriver.Chrome(service=service, options=options)
        browser.get('https://duckduckgo.com/')
        browser.implicitly_wait(10)
        title = browser.title
        search_field = browser.find_element(By.CSS_SELECTOR, "input.searchbox_input__bEGm3")
        search_field.send_keys("panda")
        search_field.send_keys(Keys.RETURN)
        time.sleep(3)
        result_title = browser.title
        input_field = browser.find_element(By.CSS_SELECTOR, "#search_form_input")
        keyword = input_field.get_attribute("value")
        link_titles = browser.find_elements(By.CSS_SELECTOR, 'a > span.EKtkFWMYpwzMKOYr0GYm')
        self.soft_assert(self.assertTrue, title.__contains__('Duck'))
        self.soft_assert(self.assertIsNot, search_field, None)
        self.soft_assert(self.assertTrue, result_title.__contains__('panda'))
        self.soft_assert(self.assertEqual, keyword, "panda")
        for link_title in link_titles:
            title = link_title.text.lower()
            self.soft_assert(self.assertTrue, title.__contains__('panda'))
        self.assert_all()