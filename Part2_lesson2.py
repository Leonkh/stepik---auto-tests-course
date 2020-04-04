import math

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int((browser.find_element_by_id("num1").text))
    y = int((browser.find_element_by_id("num2").text))

    print(x)
    print(y)
    
    z = str(x + y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла