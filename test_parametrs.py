import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('URL', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_take_number(browser, URL):
    link = f"{URL}"
    browser.get(link)
    browser.implicitly_wait(10)
    answer = math.log(int(time.time()))
    input1 = browser.find_element_by_id("ember68")
    input1.send_keys(str(answer))

    # stoptime = WebDriverWait(browser, 5).until(
    #     EC.element_to_be_clickable((By.tag_name, "button")))

    button1=browser.find_element_by_tag_name('button')
    button1.click()
    # time.sleep(5)
    text1=browser.find_element_by_class_name("smart-hints__hint").text
    text2="Correct!"
    assert text1 == text2
    time.sleep(3)
