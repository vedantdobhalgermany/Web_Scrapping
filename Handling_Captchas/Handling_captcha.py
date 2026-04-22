from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Here I used input() function , in which we manually enter the captcha and hit enter to solve the Captcha

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://www.hackthissite.org/user/login'
driver.get(url)
time.sleep(2)

username_field = driver.find_element(By.NAME,'username')
password_field = driver.find_element(By.NAME,'password')
login_button = driver.find_element(By.XPATH,"//input[@value='Login']")

username_field.send_keys('abcd')
password_field.send_keys('1234')
login_button.click()


captcha_xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/form/table/tbody/tr[5]/td/img'
captcha_element = driver.find_element(By.XPATH,captcha_xpath)
if captcha_element :
    x = input("This will halt the script....solve your Captcha")

print('\n captcha handled')


driver.quit()
