from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

current_dir = os.path.abspath(os.path.dirname(__file__))

import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    
    browser.find_element(By.TAG_NAME, 'button').click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)  

    x = browser.find_element(By.ID, 'input_value').text
    answer = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(answer)

    browser.find_element(By.CLASS_NAME, 'btn').click()

# Завершаем работу.
finally:
    time.sleep(5)
    browser.quit()