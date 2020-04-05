import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

class Testform(unittest.TestCase):
    def test_forms1(self):
        link = "http://suninjuly.github.io/registration1.html"
        
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input5 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        input5.send_keys("JJmd@kasf.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(2)

        text1 = browser.find_element_by_css_selector("div.container>h1").text
        expectedText = "Congratulations! You have successfully registered!"
        self.assertEqual(text1, expectedText), f"expected {expectedText} really something wrong"

    def test_forms2(self):
        link = "http://suninjuly.github.io/registration2.html"
        
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input5 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        input5.send_keys("JJmd@kasf.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(2)

        text1 = browser.find_element_by_css_selector("div.container>h1").text
        expectedText = "Congratulations! You have successfully registered!"
        self.assertEqual(text1, expectedText), f"expected {expectedText} really something wrong"


if __name__ == "__main__":
    unittest.main()
    print("All right!")
