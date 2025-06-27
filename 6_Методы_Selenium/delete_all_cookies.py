from pprint import pprint
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    url = "https://parsinger.ru/selenium/6/6.3.2/index.html"
    browser.get(url)

    # Получаем список существующих кук до удаления
    print("Cookies before deletion:")
    pprint(browser.get_cookies())

    # Удаляем все куки
    browser.delete_all_cookies()

    # Проверяем, что куки удалены
    print("\nCookies after deletion:")
    pprint(browser.get_cookies())

    time.sleep(10)

    browser.save_screenshot("2.jpg")