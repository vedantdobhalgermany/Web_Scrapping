from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert"
driver.get(url)

wait = WebDriverWait(driver, 10)

# Declining cookies
iframe_element = wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="fast-cmp-iframe"]')))

decline_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fast-cmp-form"]/span/button')))
decline_button.click()

driver.switch_to.default_content()

# working with alerts

iframe_element = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID,"iframeResult")))


button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='myFunction()']")))
button.click()

print(f"Alert Text: {driver.switch_to.alert.text}")

driver.switch_to.alert.accept()

driver.switch_to.default_content()

driver.quit()