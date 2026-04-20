import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://github.com/login'

driver.get(url)

# Page Object Model(POM)
# page -> class
# elements -> attributes
# interactions -> methods

class LoginPage:
    
    # Attributes
    def __init__(self,driver):
        self.driver = driver
        self.username = (By.ID, "login_field")
        self.password = (By.ID,"password")
        self.login_button = (By.NAME,"commit")

    # Methods
    def login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()

login_page = LoginPage(driver)
login_page.login("vedant","password123")

time.sleep(2)
driver.quit() 