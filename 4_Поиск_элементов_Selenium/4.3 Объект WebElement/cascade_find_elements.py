from selenium import webdriver
from selenium.webdriver.common.by import By

# Импорт модуля time для работы с задержками
import time

# Запустим браузер (например, Chrome)
with webdriver.Chrome() as driver:

  # Запустим браузер (например, Chrome)
  driver = webdriver.Chrome()

  # Перейдем на нужную страницу
  driver.get("https://parsinger.ru/selenium/3/3.3.1/index.html")

  button = driver.find_element(By.CSS_SELECTOR, "#parent_id > div:nth-child(1)").click()

  password = driver.find_element(By.CSS_SELECTOR, "#parent_id > div:nth-child(1)").get_attribute("password")

  print(password)

  # Закроем браузер
  driver.quit()