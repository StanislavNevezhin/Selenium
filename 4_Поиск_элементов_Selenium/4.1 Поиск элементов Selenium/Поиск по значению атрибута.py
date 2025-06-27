# Найти элемент по его значению
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://parsinger.ru//html/index4_page_1.html")

# Поиск элементов по атрибуту name
elements_by_name = browser.find_elements(By.NAME, '4_1')

# Проходим по каждому элементу и выводим его атрибут href
for element in elements_by_name:
    print(element.get_attribute('href'))  # правильно используем метод get_attribute() для текущего элемента

# Пауза на 5 секунд
time.sleep(5)

# Закрытие браузера
browser.quit()