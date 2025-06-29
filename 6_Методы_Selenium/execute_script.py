import time
from selenium import webdriver
from selenium.webdriver.common.by import By



with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.5/index.html')
    
    element = browser.find_element(By.XPATH, "//*[@id='target']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    
    button = browser.find_element(By.XPATH, "//*[@id='target']").click()
    time.sleep(10)

    key = browser.find_element(By.XPATH, "//*[@id='secret-key']")
    time.sleep(10)
    
    print(key.text)