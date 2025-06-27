import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Запускаем браузер Chrome
with webdriver.Chrome() as browser:
    # Открываем страницу
    browser.get('http://parsinger.ru/selenium/3/3.html')
    
    # Находим элементы форм на странице
    elements = browser.find_elements(By.XPATH, "//div/p[2]")
    
    values = []
    for element in elements:
      value = element.text
      if value.isdigit():
        values.append(int(value))  # Преобразование в целое число
    
# Подсчет общей суммы
total_sum = sum(values)

print(f"Сумма значений: {total_sum}")