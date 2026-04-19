from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

url = 'https://en.wikipedia.org/wiki/Machine_learning'

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(url)
time.sleep(2)

# scrolling by element
ai_path = '//*[@id="Artificial_intelligence"]'
ai_subtopic = driver.find_element(By.XPATH,ai_path)
driver.execute_script("arguments[0].scrollIntoView();",ai_subtopic)
time.sleep(3)


# scrolling vertically
driver.execute_script("window.scrollBy(0,2500);")
time.sleep(3)

driver.execute_script("window.scrollBy(0,-1500);")
time.sleep(2)


# scrolling to page height
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(3)
driver.execute_script("window.scrollTo(0,-document.body.scrollHeight);")

time.sleep(5)
driver.quit()