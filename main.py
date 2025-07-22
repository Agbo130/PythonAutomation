from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Setup headless Chrome
options = Options()
options.add_argument('--headless')  # run in background
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver_path = os.path.join(os.getcwd(), "chromedriver")
service = Service(driver_path)

driver = webdriver.Chrome(service=service, options=options)

# ✅ Open DuckDuckGo instead of Google
driver.get("https://duckduckgo.com")
wait = WebDriverWait(driver, 10)

# ✅ Wait and find the input box
search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))

# ✅ Type and search
search_box.send_keys("Python automation")
search_box.send_keys(Keys.RETURN)

print("✅ DuckDuckGo search automation completed (headless)")
time.sleep(3)
driver.quit()
