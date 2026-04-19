from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://miniclip.com/careers/vacancies'

driver.get(url)
time.sleep(1)

department_field = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/section[2]/div/fieldset[3]/select')
department_dropdown = Select(department_field)
department_dropdown.select_by_visible_text('Technology')

location_field = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/section[2]/div/fieldset[2]/select')
location_dropdown = Select(location_field)
location_dropdown.select_by_visible_text('Zoetermeer, Netherlands')

time.sleep(10)

driver.quit()