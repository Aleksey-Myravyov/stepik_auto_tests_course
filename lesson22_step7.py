from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

browser = webdriver.Chrome()
browser.get('')

try:
    pass

except Exception as e:
    print(f"{type(e).__name__}: {e}")

# Завершаем работу.
finally:
    time.sleep(5)
    browser.quit()