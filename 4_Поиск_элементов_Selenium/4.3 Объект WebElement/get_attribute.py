# Найти элемент по его ID
from selenium import webdriver
from selenium.webdriver.common.by import By

# Импорт модуля time для работы с задержками
import time

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/3/3.2.4/index.html")

button = browser.find_element(By.ID, 'secret-key-button').click()

password = browser.find_element(By.ID, 'secret-key-button').get_attribute("data")

print(password)

# Пауза на 5 секунд, чтобы страница успела загрузиться
time.sleep(5)

# Закрытие браузера
browser.quit()