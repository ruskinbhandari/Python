import time
from datetime import datetime
import subprocess
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://dev-02.wlink.com.np/celon/php7/ftth/index.php/login")

time.sleep(1.5)
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/form/ul/li[1]/input' ).send_keys('ruskin.bhandari')
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/form/ul/li[2]/input').send_keys('WLINk123$$$')
driver.find_element(By.XPATH, '//*[@id="main_content"]/div[2]/div/form/ul/input').click()
time.sleep(1.5)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/div[7]/button').click()
time.sleep(1.5)
driver.find_element(By.XPATH, '//*[@id="navigation"]/div[7]/div/div[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="navigation"]/div[7]/div/div[2]/ul/li[2]/a').click()

# Wait for the wrapper element to be present
wrapper_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="DataTables_Table_0_wrapper"]'))
)

# Wait for the button to be clickable
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[10]/a/button'))
)
# Click on the button
button.click()
time.sleep(2)

# Switch to the new window or tab
driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.XPATH, '//*[@id="accept"]').click()

# To Accept the browser Alert
wait = WebDriverWait(driver, 10)
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

# Get the text of the alert (optional)
alert_text = alert.text
print("Alert text:", alert_text)

# Accept (click OK) on the alert
alert.accept()

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

# Get the text of the alert (optional)
alert_text = alert.text
print("Alert text:", alert_text)

# Accept (click OK) on the alert
alert.accept()

time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="transfer"]').click()
# To Accept the browser Alert
wait = WebDriverWait(driver, 10)
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

# Get the text of the alert (optional)
alert_text = alert.text
print("Alert text:", alert_text)

# Accept (click OK) on the alert
alert.accept()

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

# Get the text of the alert (optional)
alert_text = alert.text
print("Alert text:", alert_text)

# Accept (click OK) on the alert
alert.accept()

