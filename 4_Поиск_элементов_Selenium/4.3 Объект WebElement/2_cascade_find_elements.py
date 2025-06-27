from selenium import webdriver
from selenium.webdriver.common.by import By

# Импорт модуля time для работы с задержками
import time

# Запустим браузер (например, Chrome)
with webdriver.Chrome() as driver:

  # Перейдем на нужную страницу
  driver.get("https://parsinger.ru/selenium/3/3.3.2/index.html")

  # Найдем все кнопки
  elements = driver.find_elements(By.CSS_SELECTOR, ".block button")

  # Нажмем каждую кнопку
  for element in elements:
      element.click()

  password = driver.find_element(By.CSS_SELECTOR, "body > password").text

  print(password)

      # Пауза на 5 секунд, чтобы страница успела загрузиться
  time.sleep(5)