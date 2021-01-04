from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
import time

userid=input("Enter your username: ")
passwd=getpass("\nEnter your password: ")

browser=webdriver.Chrome('/home/mumu/Documents/Automation/chromedriver')
browser.maximize_window()
browser.get('http://www.google.com')
search=browser.find_element_by_name('q')
search.send_keys("facebook")
search.send_keys(Keys.RETURN)
select=browser.find_element_by_class_name('LC20lb')
select.click()

user = WebDriverWait(browser,50).until(EC.presence_of_element_located((By.XPATH,'//input[@id="email"]')))
user.send_keys(userid)