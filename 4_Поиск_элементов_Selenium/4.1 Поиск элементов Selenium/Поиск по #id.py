# Найти элемент по его уникальному id
from selenium import webdriver
from selenium.webdriver.common.by import By

# Импорт модуля time для работы с задержками
import time

browser = webdriver.Chrome()
browser.get("https://parsinger.ru/html/headphones/5/5_1.html")
element_by_id = browser.find_element(By.ID, 'brand')

# Выведем содержимое элемента
print(element_by_id.text)

# Пауза на 5 секунд, чтобы страница успела загрузиться
time.sleep(5)

# Закрытие браузера
browser.quit()