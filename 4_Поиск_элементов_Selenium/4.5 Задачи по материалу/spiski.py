import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Запускаем браузер Chrome
with webdriver.Chrome() as browser:
    # Открываем страницу
    browser.get('http://parsinger.ru/selenium/7/7.html')
    
    # Находим элементы форм на странице
    elements = browser.find_elements(By.TAG_NAME, 'option')
    
    values = []
    for element in elements:
      value = element.text
      if value.isdigit():
        values.append(int(value))  # Преобразование в целое число
    
    # Подсчет общей суммы
    total_sum = sum(values)
    print(f"Сумма значений: {total_sum}")

    form = browser.find_element(By.ID, 'input_result').send_keys(total_sum)

    button = browser.find_element(By.CLASS_NAME, "btn").click()

    # Пауза для визуального контроля
    time.sleep(5)
    
    # Завершение работы браузера
    browser.quit()