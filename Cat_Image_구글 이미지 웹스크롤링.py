from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

url = "https://www.google.com/imghp?hl=ko&ogbl"

CHROME_DRIVER_PATH = './chromedriver.exe'
service = Service(executable_path=CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get(url)
search_field = driver.find_element(By.CSS_SELECTOR, "textarea.gLFyf")

search_field.send_keys("고양이")
search_field.send_keys(Keys.RETURN)

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height: #스크롤을 제일 하단으로 내림
        try:
            driver.find_element(By.CSS_SELECTOR, ".LZ4I").click() #결과 더 보기 버튼 클릭
        except:
            break
    last_height = new_height

images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i.Q4LuWd")

# 디렉토리 생성
os.mkdir('cat_images')

for i, image in enumerate(images):
    try:
        image.click()
        time.sleep(1)
        
        img = driver.find_element(By.CSS_SELECTOR, "img.sFlh5c")
        img_url = img.get_attribute("src")
        urllib.request.urlretrieve(img_url, f'cat_images/pic{i}.jpg')
    except:
        print('except')
        pass