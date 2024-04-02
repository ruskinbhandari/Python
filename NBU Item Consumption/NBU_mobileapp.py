import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Custom mobile emulation settings
mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 760, "pixelRatio": 4.0},
    # User agent for a browser on Android 10
    "userAgent": "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36"
}

options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=options)
# Continue with your test setup and actions

# Navigate to the website
driver.get("https://dev-02.wlink.com.np/celon/api-int-mobile/index.php/ItemConsumption/dashboard?username=rojan.thapa1&token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJyb2phbi50aGFwYTEiLCJyZWdpb25faWQiOiI0IiwiZGV2aWNlX2lkIjoiYWI1MzI2YzA1N2JjZmQ2MmMwMjU5YzQyY2Y4Y2RiN2Q4ODY3ZTdlNjU4NjdmOTIzN2JhYjM0YzBkNTE4ZDk1NXJvamFuLnRoYXBhMSIsImRlc2lnbmF0aW9uIjoiRmllbGQgQXNzaXN0YW50IiwiZWJpbGxfYnJhbmNoX2lkIjoiMTcxIiwib3duZXJzaGlwIjpudWxsLCJicmFuY2hfaWQiOjE4MSwicGhvdG9fbGluayI6Imh0dHBzOi8vc2VydmljZS1zbXNjYXN0LndsaW5rLmNvbS5ucC91c2VyX3Byb2ZpbGVzLzJiM2U0Y2VhLTM1NjAtNGUyNC04NTQ3LTgwYTVjNTQwYjUyNC5qcGciLCJicmFuY2giOiJSZWdpb24tNCBOQlUtMSIsImlhdCI6MTcxMTM0MTkwNSwiZXhwIjoxNzExOTQ2NzA1fQ.NLBw0DKy8lVyJftAoFlHKjRhMzpy3bFgC-FIhW6DLQeVaBze_mRDdSHXgQmHjVnQXZDfqmZQ14JJ2yIPMphUn0VngKkusZkl3kPjyZjJJloB6QzzrebShx1PDOmnaOmRLArRBggRuxopF64-5VwL7ELGBK2NTykL0ad63dVA74geii8NI8BYu0_W8kpUl6DsoKv0SBw328BJ9rVbRVAYbly0IYJw52t7I9uDy6JpxmTEzhjKDubNmImoBIy9CU3kvo0DO4dxc9bMrdzHUwO2DI6Hm0YsbV-4Nqjoo9LAJxm2OI1zplNmJa23dj63Wl3mk4rXrVBtwjgTavRnc_PjXQ&deviceId=ab5326c057bcfd62c0259c42cf8cdb7d8867e7e65867f9237bab34c0d518d955rojan.thapa1")

time.sleep(1.5)
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, '/html/body/div/div/div/section' )
driver.find_element(By.XPATH, '/html/body/div/div/div/section/div/div/div/a[1]' ).click()
driver.find_element(By.XPATH, '/html/body/div/div/div/section/div[1]/div/div/div/a' ).click()
driver.find_element(By.XPATH, '//*[@id="title"]').send_keys('Test NBU Item Consumption')

driver.find_element(By.XPATH, '//*[@id="locator_branch"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/section/div/div/form/div/div[3]/div/select/option[5]').click()
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('thapa.subash')
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="ui-id-3"]' ).click()
time.sleep(2)

#driver.find_element(By.XPATH, '//*[@id="items"]').send_keys('QR Code For Splitter Box')
#time.sleep(10)
#driver.find_element(By.XPATH, '//*[@id="ui-id-5"]' ).click()
element = driver.find_element(By.XPATH, '//*[@id="items"]')
element.send_keys('12 Core ADSS Fiber')
time.sleep(12)
element.send_keys(Keys.DOWN, Keys.ENTER)

driver.find_element(By.XPATH, '//*[@id="quantity"]').send_keys(1)
driver.find_element(By.XPATH, '//*[@id="description"]').send_keys('NBU Item Consumption Test')
driver.find_element(By.XPATH, '//*[@id="reason"]').send_keys('Test at NBU Item Consumption')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="submit"]/b').click()
time.sleep(2)
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

input("Press Enter to close the browser...") #Hold Browser
driver.quit()  # This line will only execute after you press Enter