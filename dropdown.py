from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
import math
def sum(x, y):
    return str(x + y)

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1")
    x = int(x.text)
    y = browser.find_element(By.ID, "num2")
    y = int(y.text)
    z = sum(x, y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z) 
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
