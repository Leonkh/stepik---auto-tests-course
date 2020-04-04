from selenium import webdriver
import time
import math
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    
    input1 = browser.find_element_by_css_selector('.form-group>:nth-child(2)')
    input1.send_keys("Alex")

    input2 = browser.find_element_by_css_selector('.form-group>:nth-child(4)')
    input2.send_keys("Bro")

    input3 = browser.find_element_by_css_selector('.form-group>:nth-child(6)')
    input3.send_keys("sfsdf@gmail.com")

    # option1 = browser.find_element_by_id("robotCheckbox")
    # option1.click()

    current_dir = os.path.abspath(os.path.dirname("/Users/leonidhabibullin/selenium_course/"))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, '1.txt')

    element = browser.find_element_by_css_selector("[type='file']")
    element.send_keys(file_path)

    buttom = browser.find_element_by_css_selector("[type='submit']")
    buttom.click()

finally:
    time.sleep(20)
    browser.quit()


# не забываем оставить пустую строку в конце файла