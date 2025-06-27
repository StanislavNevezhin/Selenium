import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Запускаем браузер Chrome
with webdriver.Chrome() as browser:
    # Открываем страницу
    browser.get('https://parsinger.ru/selenium/1/1.html')
    
    # Находим элементы форм на странице
    forms = browser.find_elements(By.XPATH, "//*[@class='form']")
    
    # Заполняем каждое поле формы
    for form in forms:
        form.send_keys("Текст")
    
    # Нажимаем кнопку с классом btn
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    
    # Немедленно читаем результат (без ожидания)
    result = browser.find_element(By.ID, "result").text
    print(result)
    
    # Пауза для визуального контроля
    time.sleep(5)