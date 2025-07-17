import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Вычисляем зашифрованное значение
link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

# Открываем браузер
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")

try:
    # Находим ссылку по полному тексту и кликаем
    link = browser.find_element(By.LINK_TEXT, link_text)
    link.click()

    # Заполняем форму на открывшейся странице
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Имя")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Фамилия")

    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Город")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Страна")

    # Отправляем форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждём, чтобы успеть скопировать код
    time.sleep(10)

finally:
    browser.quit()
