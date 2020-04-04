from selenium import webdriver
import time
import math
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    buttom = browser.find_element_by_css_selector("[type='submit']")
    buttom.click()
    
    alert = browser.switch_to.alert
    alert.accept()

    x = int(browser.find_element_by_id('input_value').text)
    y = str(math.log(abs(12*math.sin(x))))

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    buttom = browser.find_element_by_css_selector("[type='submit']")
    buttom.click()

finally:
    time.sleep(20)
    browser.quit()


# не забываем оставить пустую строку в конце файла