from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/registration2.html')
    
    # Создаем список элементов с обязательным заполнением. Аттрибут - required.
    list_inputs = browser.find_elements(By.CSS_SELECTOR, '[required]')
    
    # Циклом for заполняем все обязательные поля словом 'Check'
    for i in list_inputs:
        i.send_keys('Check')
    
    # Отправляем заполненную форму. 
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    
    time.sleep(1)
    checking = browser.find_element(By.TAG_NAME, 'h1').text  
    # Проверяем результат.  
    assert "Congratulations! You have successfully registered!" == checking
    
# Выводим сообщения об ошибке с подробным описанием.
except Exception as e:
    print(f"{type(e).__name__}: {e}")

# Завершаем работу.
finally:
    time.sleep(10)
    browser.quit()