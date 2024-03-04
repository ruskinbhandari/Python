import time
import subprocess
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


driver.get("https://dev-02.wlink.com.np/celon/tt/login")

driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('ruskin.bhandari')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('WLInk123$$$')
driver.find_element(By.XPATH, '/html/body/section/form/p[3]/button').click()

driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/a').click()
driver.find_element(By.XPATH, '/html/body/div/button[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/div[1]/li[4]/a').click()

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="datatable_wrapper"]')
driver.find_element(By.XPATH,'//*[@id="table-body"]/tr[1]/td[11]/a/button').click()
driver.find_element(By.XPATH,'//*[@id="accept"]').click()

wait = WebDriverWait(driver, 10)
#driver.find_element(By.ID, "OKButton").OK_button.click()
#OK_button = driver.find_element(By.NAME, "OK").click()
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

driver.find_element(By.XPATH,'//*[@id="transfer"]').click()
wait = WebDriverWait(driver, 10)
#driver.find_element(By.ID, "OKButton").OK_button.click()
#OK_button = driver.find_element(By.NAME, "OK").click()
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

time.sleep(5)

driver.find_element(By.XPATH,'//*[@id="historymodalbutton"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="historymodal"]/div/div/div[1]/button/i').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="message"]').send_keys('Approved and demand transferred')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="messagesubmit"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]')
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]').click()
