from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    
    button = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button2 = browser.find_element_by_id('book')
    button2.click()

    x = int(browser.find_element_by_id('input_value').text)
    y = str(math.log(abs(12*math.sin(x))))

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    button3 = browser.find_element_by_css_selector("[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button3)
    browser.execute_script("window.scrollBy(0, 100);")
    button3.click()

    time.sleep(10)
finally:
    time.sleep(5)
    browser.quit()
