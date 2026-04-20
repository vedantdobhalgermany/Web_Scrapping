from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://www.google.com'

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(url)
time.sleep(1)

# clicking button
all_abhelen_button = '//*[@id="W0wltc"]/div'
button_click = driver.find_element(by=By.XPATH,value = all_abhelen_button)
button_click.click()


search_bar_path = '//*[@id="APjFqb"]'
search_bar = driver.find_element(By.XPATH,search_bar_path)

search_bar.send_keys("machine learning")

wait = WebDriverWait(driver,20)
wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[4]/form/div[1]/div[1]/div[3]/center/input[1]')))

search_bar.send_keys(Keys.ENTER)


time.sleep(2)
driver.quit()