import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='module')
def driver():
    CHROME_DRIVER_PATH = './chromedriver.exe'
    service = Service(executable_path=CHROME_DRIVER_PATH)
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)

    yield browser

    browser.close()