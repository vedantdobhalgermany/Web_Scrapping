from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.google.com"

driver.get(url)
print(f"Title :{driver.title}")
print(f"URL :{driver.current_url}")

driver.save_screenshot("google-screenshot.png")
print("screenshot done")

driver.quit()