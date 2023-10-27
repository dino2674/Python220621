from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import openpyxl as op


url = "http://ccdome.co.kr/"

CHROME_DRIVER_PATH = './chromedriver.exe'
service = Service(executable_path=CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)

browser.get(url)
browser.implicitly_wait(2) # 로딩 대기

container = browser.find_element(By.CSS_SELECTOR, 'div.container')
containerList = container.find_element(By.CSS_SELECTOR, 'ul > li')

print(containerList)

# id_field = browser.find_element(By.CSS_SELECTOR, 'loginId')
# id_field.send_keys("lya1417")
 
# pwd_field = browser.find_element(By.CSS_SELECTOR, 'loginPwd')
# pwd_field.send_keys("young9689!")