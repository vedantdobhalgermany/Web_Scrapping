from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

url1 = "https://www.google.com"

driver.get(url1)

time.sleep(1)

# clicking button
all_abhelen_button = '//*[@id="W0wltc"]/div'
button_click = driver.find_element(by=By.XPATH,value = all_abhelen_button)
button_click.click()

search_bar_xpath ='//*[@id="APjFqb"]'
search_bar = driver.find_element(by=By.XPATH, value = search_bar_xpath)


#clearing text
search_bar.clear()

# entering text
search_bar.send_keys("machine learning")
time.sleep(1)

# clicking key
search_bar.send_keys(Keys.ENTER)

time.sleep(3)

driver.quit()


## Another website 

driver = webdriver.Chrome()
driver.maximize_window()

url2 = 'https://github.com/login'

driver.get(url2)

time.sleep(1)

# user_id
user_id = driver.find_element(By.ID,'login_field')
user_id.send_keys('Vedantdobhal')

# password
password = driver.find_element(By.ID,'password')
password.send_keys('123$%%^yuio')

# submit button
button_path = '/html/body/div[1]/div[4]/main/div/div[2]/form/div[3]/input'
submit_button = driver.find_element(by=By.XPATH,value=button_path)
submit_button.click()

time.sleep(3)

driver.quit()