from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_target"
driver.get(url)
time.sleep(2)

wait = WebDriverWait(driver, 10)


iframe_element = wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="fast-cmp-iframe"]')))

decline_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fast-cmp-form"]/span/button')))
decline_button.click()

driver.switch_to.default_content()

iframe_element2 = wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="iframeResult"]')))

link = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/p[1]/a')))
link.click()
time.sleep(2)


driver.switch_to.default_content()

time.sleep(5)
driver.quit()