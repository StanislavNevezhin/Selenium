import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Запуск браузера Chrome
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/2/1.html')
    
    # Найти все поля ввода на странице
    fields = browser.find_elements(By.XPATH, "//input[@data-enabled='true']")
    
    # Пройтись по каждому полю и очистить его
    for field in fields:
        field.clear()
    
    # Нажимаем кнопку
    button = browser.find_element(By.XPATH, "//*[@id='checkButton']")
    button.click()
    
    # Ожидаем появление alert-а
    wait = WebDriverWait(browser, 3)
    alert = wait.until(EC.alert_is_present())
    
    # Читаем сообщение из alert-a
    secret_code = alert.text
    print(f"Секретный код: {secret_code}")
    
    # Закрываем alert
    alert.accept()