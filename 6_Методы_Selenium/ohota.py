# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

# # Создаем объект ChromeOptions
# chrome_options = Options()

# # Добавляем аргументы командной строки
# chrome_options.add_argument('--headless=new')       # Без графического интерфейса
# chrome_options.add_argument('--no-sandbox')     # Отключение песочницы

# # Запускаем браузер с использованием указанных настроек
# browser = webdriver.Chrome(options=chrome_options)

# try:
#     browser.get('https://parsinger.ru/methods/1/index.html')

#     for i in range(500):
#         browser.refresh()
#         element = browser.find_element(By.XPATH, "//*[@id='result']")
#         print(element.text)
# finally:
#     browser.quit()  # Закрываем браузер после завершения работы


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    
    for _ in range(500):
        browser.refresh()
        
        # Пытаемся найти элемент с текстом
        elements = browser.find_elements(By.XPATH, "//*[@id='result']")
        
        if len(elements) > 0:
            result_text = elements[0].text.strip()  # Убираем пробелы вокруг текста
            
            # Проверяем, является ли текст числа
            if result_text.isdigit():  # Проверяем, что строка состоит только из цифр
                print("Элемент найден:", result_text)
                break  # Останавливаем цикл