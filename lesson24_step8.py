from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    
    # Ждем когда появиться необходимое число.
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100')) 

    # Нажимаем на кнопку Book
    browser.find_element(By.TAG_NAME, 'button').click()
    
    # Прокручиваем вниз.
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Вводим ответ в строку.
    x = browser.find_element(By.ID, 'input_value').text
    answer = calc(x)
    browser.find_element(By.NAME, 'text').send_keys(answer)
    browser.find_element(By.ID, 'solve').click()


# Завершаем работу.
finally:
    time.sleep(5)
    browser.quit()