import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Запускаем браузер Chrome
with webdriver.Chrome() as browser:
    # Открываем страницу
    browser.get('http://parsinger.ru/selenium/6/6.html')
    
    # Находим элементы форм на странице
    expression = browser.find_element(By.ID, 'text_box').text
    
    result = eval(expression)
    print(result)

    # Находим элементы форм на странице
    elements = browser.find_elements(By.TAG_NAME, 'option')
    
    for element in elements:
      value = element.text
      if int(value) == result:
        element.click()
    
    # Нажимаем кнопку с классом btn
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    
    # Пауза для визуального контроля
    time.sleep(5)