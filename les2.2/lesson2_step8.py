from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_firstname = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input_firstname.send_keys("Nikita")
    input_lastname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input_lastname.send_keys("Nikita")
    input_email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input_email.send_keys("Nikita")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    input_file = browser.find_element(By.ID, "file")
    input_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()