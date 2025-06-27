import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Запускаем браузер Chrome
with webdriver.Chrome() as browser:
    # Открываем страницу
    browser.get('http://parsinger.ru/selenium/4/4.html')
    
    # Находим элементы форм на странице
    forms = browser.find_elements(By.XPATH, "//*[@class='check']")
    
    # Заполняем каждое поле формы
    for form in forms:
        form.click()
    
    # Нажимаем кнопку с классом btn
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    
    # Немедленно читаем результат (без ожидания)
    result = browser.find_element(By.ID, "result").text
    print(result)
    
    # Пауза для визуального контроля
    time.sleep(5)