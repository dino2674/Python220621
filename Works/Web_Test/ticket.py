from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui


CHROME_DRIVER_PATH = './chromedriver.exe'
service = Service(executable_path=CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)
browser.get('https://www.ticketlink.co.kr/home')
browser.implicitly_wait(10)


pyautogui.moveTo(1021, 240, duration=0.5)
pyautogui.click(clicks=2, interval=0.2, button='left')

browser.implicitly_wait(10)

pyautogui.moveTo(135, 300, duration=0.1)
pyautogui.click(clicks=2, interval=0.2, button='left')
pyautogui.write('yjsong9689@gmail.com', interval=0.2)

pyautogui.moveTo(96, 346, duration=0.1)
pyautogui.click(clicks=2, interval=0.2, button='left')
pyautogui.write('Young9689.', interval=0.2)

#로그인 버튼 클릭
pyautogui.moveTo(189, 419, duration=0.1)
pyautogui.click(clicks=2, interval=0.2, button='left')
time.sleep(3)

#스포츠 버튼 클릭
pyautogui.moveTo(618, 301, duration=0.1)
pyautogui.click(clicks=2, interval=0.2, button='left')

#축구 버튼 클릭
pyautogui.moveTo(394, 377, duration=0.1)
pyautogui.click(clicks=2, interval=0.2, button='left')
time.sleep(1)

#대구 FC 버튼 클릭
pyautogui.moveTo(361, 831, duration=0.1)
pyautogui.click(clicks=2, interval=0.2, button='left')
time.sleep(3)

#예매하기 버튼 클릭
pyautogui.moveTo(1242, 827, duration=0.1)
pyautogui.click(clicks=2, interval=0.2, button='left')
time.sleep(3)

pyautogui.moveTo(188, 662, duration=0.1)
pyautogui.click(clicks=2, interval=0.2, button='left')
time.sleep(3)

pyautogui.moveTo(367, 670, duration=0.1)
pyautogui.click(clicks=2, interval=0.2, button='left')
time.sleep(3)

print(pyautogui.size())
print(pyautogui.position())
pyautogui.mouseInfo()  



time.sleep(10)
