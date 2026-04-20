from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_target")
time.sleep(3)

# Step 1: Dismiss cookie/privacy popup
driver.execute_script("""
    var btn = document.getElementById('didomi-notice-disagree-button');
    if (btn) btn.click();
""")
time.sleep(1)

wait = WebDriverWait(driver, 10)

# Step 2: Switch into the outer result iframe (#iframeResult)
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframeResult")))
print("✅ Switched into #iframeResult")

# Step 3: Switch into the nested iframe (the embedded W3Schools site)
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='W3Schools Free Online Web Tutorials']")))
print("✅ Switched into nested W3Schools iframe")

# Step 4: Interact with content inside the nested iframe
# Example: click the "Learn HTML" button on the W3Schools homepage
learn_html_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Learn HTML')]"))
)
learn_html_btn.click()
print("✅ Clicked 'Learn HTML' link inside nested iframe")

time.sleep(60)
driver.quit()