import time
import subprocess
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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
driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/div[1]/li[2]/a').click()

driver.find_element(By.XPATH, '/html/body/div[1]/a/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="multibranchmodal"]/div/div/div[2]')
driver.find_element(By.XPATH, '//*[@id="multibranch"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="multibranch"]/option[3]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="title"]').send_keys('NOC Item Consumption Consumption')
driver.find_element(By.XPATH, '//*[@id="consumption_type"]')
driver.find_element(By.XPATH, '//*[@id="consumption_type"]/option[2]').click()
driver.find_element(By.XPATH, '//*[@id="sub_consumption_type"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="sub_consumption_type"]/option[2]').click()

driver.find_element(By.XPATH, '//*[@id="item-section"]/div[1]/div[2]/div/div[1]/input')
driver.find_element(By.XPATH, '//*[@id="item-section"]/div[1]/div[2]/div/div[1]/input').send_keys('POWER STRIP 6 WAY')
time.sleep(9)
driver.find_element(By.XPATH, '//*[@id="ui-id-2"]').click()
driver.find_element(By.XPATH, '//*[@id="item-section"]/div[1]/div[2]/div/div[3]/input').send_keys('1')
driver.find_element(By.XPATH, '//*[@id="items-0-reason"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="items-0-reason"]/option[2]').click()
driver.find_element(By.XPATH, '//*[@id="items-0-field"]').click()
driver.find_element(By.XPATH, '//*[@id="items-0-field"]/option[11]').click()
driver.find_element(By.XPATH, '//*[@id="items-0-consumption_sub_field"]/option[2]').click()
driver.find_element(By.XPATH, '//*[@id="items-0-conusmption_field_detail"]').send_keys('NOC Item Consumption Consumption field')
driver.find_element(By.XPATH, '//*[@id="description"]').send_keys('NOC Item Consumption Consumption')
#driver.find_element(By.XPATH, '//*[@id="consumptionForm"]/div[8]/div')
#driver.find_element(By.XPATH, '//*[@id="submitAndVerify"]').click()
submit_button = driver.find_element(By.XPATH, '//*[@id="submitAndVerify"]')
ActionChains(driver).move_to_element(submit_button).click().perform()

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


