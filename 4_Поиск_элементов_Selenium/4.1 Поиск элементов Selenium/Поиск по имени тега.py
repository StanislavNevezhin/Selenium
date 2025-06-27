# Найти элемент по его tag
from selenium import webdriver
from selenium.webdriver.common.by import By

# Импорт модуля time для работы с задержками
import time

browser = webdriver.Chrome()
browser.get("https://parsinger.ru//html/index4_page_1.html")
all_elements = browser.find_elements(By.CSS_SELECTOR, 'a')

# Выведем содержимое элемента
for element in all_elements:
  print(element.text)

# Пауза на 5 секунд, чтобы страница успела загрузиться
time.sleep(5)

# Закрытие браузера
browser.quit()