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

# User Demand Request
driver.get("https://dev-02.wlink.com.np/celon/tt/login")

driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('ruskin.bhandari')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('WLInk123$$$')
driver.find_element(By.XPATH, '/html/body/section/form/p[3]/button').click()

driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/a').click()
driver.find_element(By.XPATH, '/html/body/div/button[2]/a').click()
driver.find_element(By.XPATH, '/html/body/div[1]/a/button').click()

driver.find_element(By.XPATH, '//*[@id="multibranch"]').click()
driver.find_element(By.XPATH, '//*[@id="multibranch"]/option[1]').click()
driver.find_element(By.XPATH, '//*[@id="multibranch"]/option[3]').click()

driver.find_element(By.XPATH, '//*[@id="title"]').send_keys('test demand')
driver.find_element(By.XPATH, '//*[@id="demandForm"]/div[2]/div[2]/input').send_keys('POWER STRIP 6 WAY')
time.sleep(9)
driver.find_element(By.XPATH, '//*[@id="ui-id-2"]').click()
driver.find_element(By.XPATH, '//*[@id="demandForm"]/div[2]/div[4]/input').send_keys('1')
driver.find_element(By.XPATH, '//*[@id="description"]').send_keys('NOC Item Consumption Description')
driver.find_element(By.XPATH, '//*[@id="reason"]').send_keys('NOC Item Consumption Reason')
driver.find_element(By.XPATH, '//*[@id="submitAndVerify"]').click()

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

driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/div[1]/li[1]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="datatable_wrapper"]')
driver.find_element(By.XPATH, '//*[@id="table-body"]/tr[1]/td[10]/a/button').click()

driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="message"]').send_keys('For official use')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="messagesubmit"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]')
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]').click()

# Supervisor Part
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/div[1]/li[3]/a/small').click()

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

driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="message"]').send_keys('Approved')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="messagesubmit"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]')
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]').click()
time.sleep(2)

# Logistician Part
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
time.sleep(2)

# User received part
driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/div[1]/li[1]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="datatable_wrapper"]')
driver.find_element(By.XPATH, '//*[@id="table-body"]/tr[1]/td[10]/a/button').click()
driver.find_element(By.XPATH, '//*[@id="demandForm"]')
driver.find_element(By.XPATH, '//*[@id="accept"]').click()


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
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="message"]').send_keys('Demand Received')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="messagesubmit"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]')
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]').click()

# Consumption Part
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



