from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

url = 'https://demoqa.com/select-menu'

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(url)
time.sleep(1)

cars_element = driver.find_element(By.XPATH, '//*[@id="cars"]')
cars_ms = Select(cars_element)
time.sleep(2)

cars_ms.select_by_index(1)
time.sleep(1)
cars_ms.select_by_visible_text('Opel')
time.sleep(1)
cars_ms.select_by_visible_text('Audi')
time.sleep(2)


cars_ms.deselect_by_index(1)
time.sleep(1)
cars_ms.deselect_all()

time.sleep(3)
driver.quit()