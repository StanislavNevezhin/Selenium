import time
from selenium import webdriver
from selenium.webdriver.common.by import By

cookie_dict = {
    'name': 'secretKey',    # Любое имя для cookie
    'value': 'selenium123'
}

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.3/index.html')
    browser.add_cookie(cookie_dict)
    print(browser.get_cookies())
    browser.refresh()
    time.sleep(10)
    print(browser.find_element(By.ID, "password").text)