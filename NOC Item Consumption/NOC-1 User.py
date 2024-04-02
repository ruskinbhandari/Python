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

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://dev-02.wlink.com.np/celon/php7/ftth/index.php/login")

time.sleep(1.5)
driver.maximize_window()
time.sleep(2)

# Zoom out twice
#for _ in range(3):
    # Send 'Ctrl' + '-' to zoom out
    #driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + '-')
    #driver.execute_script("document.body.style.zoom = '80%'")

driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/form/ul/li[1]/input' ).send_keys('ruskin.bhandari')
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/form/ul/li[2]/input').send_keys('WLINk123$$$')
driver.find_element(By.XPATH, '//*[@id="main_content"]/div[2]/div/form/ul/input').click()
time.sleep(1.5)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/div[7]/button').click()
time.sleep(1.5)

driver.find_element(By.XPATH, '//*[@id="navigation"]/div[7]/div/div[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="navigation"]/div[7]/div/div[1]/ul/li[2]/a').click()

driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/a/h2').click()
time.sleep(1.5)

driver.find_element(By.XPATH, '//*[@id="multiheader"]').click()
driver.find_element(By.XPATH, '//*[@id="multiheader"]/option[2]').click()

driver.find_element(By.XPATH, '//*[@id="title"]').send_keys('NOC Item Consumption')
element = driver.find_element(By.XPATH, '//*[@id="requested_for"]')
element.send_keys('ruskin.bhandari')
time.sleep(2)
# Simulate pressing the "Enter" key
element.send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="demandForm"]/div[3]/div[2]/input').send_keys('Diary')
time.sleep(7)
driver.find_element(By.XPATH, '//*[@id="ui-id-8"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="demandForm"]/div[3]/div[4]/input').send_keys('1')
driver.find_element(By.XPATH, '//*[@id="description"]').send_keys('NOC Item Consumption description')
driver.find_element(By.XPATH, '//*[@id="reason"]').send_keys('NOC Item Consumption Reason')

# Get today's date
today = datetime.today().date()

# Format today's date as MM/DD/YYYY
formatted_date = today.strftime('%m/%d/%Y')

# Print formatted date
print(formatted_date)

# Assign today's date to the current variable
current = formatted_date

# Get the current time
current_time = datetime.now().time()

# Format the current time to extract hour and minute
formatted_time = current_time.strftime('%H:%M:%S')

# Print the formatted time
print(formatted_time)

# Assign today's time to the current variable
currenttime = formatted_time

# Locate the element and send keys
element = driver.find_element(By.XPATH, '//*[@id="expected_consumption_start_date"]')
element.send_keys(current + Keys.TAB + currenttime)
# Locate the element and send keys
element = driver.find_element(By.XPATH, '//*[@id="expected_consumption_end_date"]')
element.send_keys(current + Keys.TAB + currenttime)
time.sleep(2)
element = driver.find_element(By.XPATH, '//*[@id="ho_user"]')
element.send_keys('ruskin.bhandari')
time.sleep(2)
# Simulate pressing the "Enter" key
element.send_keys(Keys.ENTER)

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="submitAndVerify"]').click()

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
