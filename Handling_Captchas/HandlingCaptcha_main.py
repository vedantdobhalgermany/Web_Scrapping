import cv2
import time 
import pytesseract
import numpy as np
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By

pytesseract.pytesseract.tesseract_cmd = r"/opt/anaconda3/bin/tesseract"

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
time.sleep(5)

try:
    captcha_xpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/form/table/tbody/tr[5]/td/img'
    captcha_image = driver.find_element(By.XPATH,captcha_xpath)
    driver.save_screenshot('webpage.png')

    location = captcha_image.location
    size = captcha_image.size
    device_pixel_ratio = driver.execute_script("return window.devicePixelRatio;")
    x = int(location['x'] * device_pixel_ratio)
    y = int(location['y'] * device_pixel_ratio)
    w = int(size['width'] * device_pixel_ratio)
    h = int(size['height'] * device_pixel_ratio)

    img = Image.open('webpage.png')
    captcha_image = img.crop((x, y, x + w, y + h))
    captcha_image.save('captcha.png')

    captcha_cv = np.array(captcha_image)
    captcha_cv = cv2.cvtColor(captcha_cv, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(captcha_cv, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 3)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((2, 2), np.uint8)
    thresh = cv2.dilate(thresh, kernel, iterations=1)
    cv2.imwrite('captcha-processed.png', thresh)

    captcha_text = pytesseract.image_to_string(Image.fromarray(thresh), config='--psm 8').strip()
    print(f'Detected captcha text: {captcha_text}')

    if captcha_text:
        username_field = driver.find_element(By.ID, 'login_username')
        password_field = driver.find_element(By.ID, 'login_password')
        captcha_field = driver.find_element(By.XPATH, '/html[1]/body[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/form[1]/table[1]/tbody[1]/tr[4]/td[2]/input[1]')
        login_button = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/form/table/tbody/tr[4]/td/input')

        username_field.clear()
        password_field.clear()
        captcha_field.clear()

        username_field.send_keys('abc')
        password_field.send_keys('1234')
        captcha_field.send_keys(captcha_text)
        login_button.click()
    else:
        print('Unable to read Captcha.')

except Exception as e:
    print('Unable to locate Captcha:', e)
finally:
    time.sleep(2)
    driver.quit()

