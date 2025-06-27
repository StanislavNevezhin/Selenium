# Найти элемент по его class
from selenium import webdriver
from selenium.webdriver.common.by import By

# Импорт модуля time для работы с задержками
import time

browser = webdriver.Chrome()
browser.get("https://parsinger.ru/html/index5_page_1.html#5_1")
all_products = browser.find_elements(By.CLASS_NAME, 'price')

# Выведем содержимое элемента
for product in all_products:
    print(product.text)



# Пауза на 5 секунд, чтобы страница успела загрузиться
time.sleep(5)

# Закрытие браузера
browser.quit()