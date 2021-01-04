from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path='/home/mumu/Documents/Automation/chromedriver')
driver.maximize_window()
driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
driver.find_element_by_xpath('//button[@data-provider="google"]').click()
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(muthaiyanmani01)
input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/span/span')))
input.click()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)

















time.sleep(1)
email=driver.find_element_by_xpath("//input[@type='email']")
email.click()
email.send_keys('muthaiyanmani01')
time.sleep(1)
email.send_keys(Keys.RETURN)
