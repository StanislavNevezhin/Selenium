from selenium import webdriver
from selenium.webdriver.common.by import By

# Запустим браузер (например, Chrome)
driver = webdriver.Chrome()

# Перейдем на нужную страницу
driver.get("https://parsinger.ru/selenium/3/3.3.3/index.html")

# Найдем все теги <a> с атрибутом stormtrooper
elements = driver.find_elements(By.CSS_SELECTOR, 'a[stormtrooper]')

# Фильтруем элементы, оставляя только те, у которых значение атрибута stormtrooper число
values = []
for element in elements:
    value = element.get_attribute('stormtrooper')
    if value.isdigit():
        values.append(int(value))  # Преобразование в целое число

# Подсчет общей суммы
total_sum = sum(values)

print(f"Сумма значений атрибута stormtrooper: {total_sum}")

field = driver.find_element(By.ID, 'inputNumber').send_keys(total_sum)

button = driver.find_element(By.ID, 'checkBtn').click()

password = driver.find_element(By.ID, 'feedbackMessage').text

print(password.split( )[1])

# Закроем браузер
driver.quit()