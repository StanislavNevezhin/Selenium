import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.1/index.html')
    cookies = browser.get_cookies()
    for cookie in cookies:
        print(f'name {cookie['name']}, value {cookie['value']}') 
        
    
# Пауза для визуального контроля
time.sleep(10)