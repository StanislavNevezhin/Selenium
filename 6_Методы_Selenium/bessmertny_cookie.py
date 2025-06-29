import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Chrome
with webdriver.Chrome() as browser:
    # Переходим на веб-страницу
    browser.get('https://parsinger.ru/methods/5/index.html')

    # Получаем список ссылок
    links = [item.get_attribute('href') for item in browser.find_elements(By.TAG_NAME, 'a')]

    # Инициализация значений для отслеживания максимальной длительности экспирации и соответствующей ссылки
    max_expiry_value = float('-inf')  # Устанавливаем минимально возможное значение
    max_expiry_link = ''

    # Перебор каждой ссылки
    for link in links:
        browser.get(link)
        
        # Получаем куки текущего домена
        cookies = browser.get_cookies()
        
        # Проверяем наличие куки с атрибутом expirty
        for cookie in cookies:
            if 'expiry' in cookie:
                expiry_value = cookie['expiry']
                
                # Обновляем максимальную длительность и ссылку, если найдено большее значение
                if expiry_value > max_expiry_value:
                    max_expiry_value = expiry_value
                    max_expiry_link = link

    # Выводим ссылку с наибольшей продолжительностью жизни куки
    browser.get(max_expiry_link)
    element = browser.find_element(By.ID,'result').text
    print(element)