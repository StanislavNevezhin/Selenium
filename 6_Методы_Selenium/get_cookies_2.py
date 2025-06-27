import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Chrome
with webdriver.Chrome() as browser:
    # Переход на веб-страницу
    browser.get('https://parsinger.ru/selenium/6/6.3/index.html')
    
    # Получение куков страницы
    cookies = browser.get_cookies()
    for cookie in cookies:
        print(f"name {cookie['name']}, value {cookie['value']}")
    
    # Берем значение последнего полученного кука
    cookie_value = cookie['name']
    
    # Заполняем форму значением кука
    form_input = browser.find_element(By.XPATH, "//*[@id='phraseInput']")
    form_input.send_keys(cookie_value)
    
    # Ждем немного для проверки заполнения формы
    time.sleep(5)
    
    # Нажимаем кнопку проверки
    check_button = browser.find_element(By.ID, "checkButton")
    check_button.click()
    
    # Получаем результат после нажатия кнопки
    result = browser.find_element(By.ID, "result").text
    
    # Печать результата
    print(result)