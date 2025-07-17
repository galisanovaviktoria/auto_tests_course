from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"  # проверь сначала на первой версии
    browser = webdriver.Chrome()
    browser.get(link)

    # УНИКАЛЬНЫЕ СЕЛЕКТОРЫ ДЛЯ ОБЯЗАТЕЛЬНЫХ ПОЛЕЙ
    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input[placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input[placeholder='Input your last name']")
    input2.send_keys("Smirnov")
    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input[placeholder='Input your email']")
    input3.send_keys("Ivan@gmail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
