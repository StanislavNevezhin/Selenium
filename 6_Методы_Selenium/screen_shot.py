import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Запускаем браузер Chrome
with webdriver.Chrome() as browser:
    # Открываем страницу
    browser.get('https://parsinger.ru/selenium/6/6.2.1/index.html')
    
    # Находим ссылки на странице
    picture = browser.find_element(By.XPATH, "//*[@id='this_pic']").click()
    
    #Делаем скриншот
    #browser.maximize_window()
    browser.save_screenshot("1.jpg")

    # Пауза для визуального контроля
    time.sleep(20)

    # # Завершение работы браузера
    # browser.quit()