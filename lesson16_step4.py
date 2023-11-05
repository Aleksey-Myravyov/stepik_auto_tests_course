from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome() # great new copy Chrome
    browser.get(link) # send a link
    
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan") # write Ivan in First name.
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Russia")
    botton = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    botton.click()
finally:
    time.sleep(30) # wait 30 seconds.
    browser.quit() # close the browser after all manipulations. 
