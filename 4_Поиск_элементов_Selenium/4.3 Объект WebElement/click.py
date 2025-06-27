# Найти элемент по его ID
from selenium import webdriver
from selenium.webdriver.common.by import By

# Импорт модуля time для работы с задержками
import time

browser = webdriver.Chrome()
browser.get("https://parsinger.ru/selenium/3/3.2.1/index.html")
button = browser.find_element(By.ID, 'clickButton').click()

# Пауза на 5 секунд, чтобы страница успела загрузиться
time.sleep(5)

# Закрытие браузера
browser.quit()