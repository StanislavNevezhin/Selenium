import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Запускаем браузер Chrome
with webdriver.Chrome() as browser:
    # Открываем страницу
    browser.get('http://parsinger.ru/selenium/2/2.html')
    
    # Находим элементы форм на странице
    link = browser.find_element(By.XPATH, "//*[text()='16243162441624']").click()
        
    # Немедленно читаем результат (без ожидания)
    result = browser.find_element(By.ID, "result").text
    print(result)
    
    # Пауза для визуального контроля
    time.sleep(5)