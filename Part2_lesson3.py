from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = int(browser.find_element_by_id("input_value").text)
    # print(x)
    y = math.log(abs(12*math.sin(x)))
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.execute_script("window.scrollBy(0, 100);")
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    
    
    button.click()

finally:
    time.sleep(10)
    browser.quit()


# не забываем оставить пустую строку в конце файла