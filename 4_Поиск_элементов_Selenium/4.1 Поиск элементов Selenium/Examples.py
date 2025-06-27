""" # Импорт модуля webdriver из библиотеки Selenium для управления браузером
from selenium import webdriver

# Импорт модуля time для работы с задержками
import time

# Создание экземпляра webdriver браузера Chrome
browser = webdriver.Chrome()

# Открытие сайта "stepik.org" в браузере
browser.get("http://stepik.org/a/104774")

# Пауза на 5 секунд, чтобы страница успела загрузиться
time.sleep(5)

# Закрытие браузера
browser.quit() """

""" # Пример того как мы будем искать элемент по двум атрибутам class и id
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
element = browser.find_element(By.CSS_SELECTOR, 'p.text#unique') """

""" # Поиск элемента с двойным классом
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
element = browser.find_element(By.CSS_SELECTOR, 'p.text.highlight') """

""" # Найти элемент по его уникальному id
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
user_div = browser.find_element(By.ID, 'user-profile') """

""" # Найти все элементы с классом 'product-card'
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
all_products = browser.find_elements(By.CLASS_NAME, 'product-card')

# Найти элемент с двумя классами 'product-card' и 'featured'
featured_product = browser.find_element(By.CSS_SELECTOR, '.product-card.featured') """

""" # Найти все ссылки и извлечь их URL
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
all_links = browser.find_elements(By.TAG_NAME, 'a')
for link in all_links:
    url = link.get_attribute('href')
    print(url) """

""" # Найти все изображения и извлечь их URL
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
all_images = browser.find_elements(By.TAG_NAME, 'img')
for img in all_images:
    img_url = img.get_attribute('src')
    print(img_url) """

""" # Извлечь описание из атрибута alt
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
image = browser.find_element(By.TAG_NAME, 'img')
description = image.get_attribute('alt')
print(description) # Вывод: Смартфон 'Модель X' черный """

""" # Извлечь текст подсказки
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
span_tag = browser.find_element(By.TAG_NAME, 'span')
full_description = span_tag.get_attribute('title')
print(full_description) # Вывод: Международный стандартный книжный номер """

""" # Найти видимый элемент
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
div = browser.find_element(By.TAG_NAME, 'div')
style_attribute = div.get_attribute('style')
if 'display: none' not in style_attribute:
    print("Элемент видим:", div.text) """

""" # Извлечь данные из data-атрибутов
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
button = browser.find_element(By.CLASS_NAME, 'add-to-cart')
product_id = button.get_attribute('data-product-id')
price = button.get_attribute('data-price')
print(f"ID товара: {product_id}, Цена: {price}") # Вывод: ID товара: 12345, Цена: 99.99 """