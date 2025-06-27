import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Запускаем браузер Chrome
with webdriver.Chrome() as browser:
    # Открываем страницу
    browser.get('https://parsinger.ru/selenium/6/6.2/index.html')
    
    # Находим ссылки на странице
    link = browser.find_element(By.XPATH, "//*[text()='Страница 2']").click()
    link = browser.find_element(By.XPATH, "//*[text()='Перейти на страницу 3']").click()    

    #Возвращаемся назад 
    browser.back()
    browser.back()

    # Пауза для визуального контроля
    time.sleep(10)

    # Немедленно читаем результат (без ожидания)
    result = browser.find_element(By.XPATH, "//*[@id='getPasswordBtn']").click()
        
    # Пауза для визуального контроля
    time.sleep(10)

    # # Завершение работы браузера
    # browser.quit()