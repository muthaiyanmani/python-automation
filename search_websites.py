from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser=webdriver.Chrome('/home/mumu/Documents/Automation/chromedriver')
browser.get('http://www.google.com')
search=browser.find_element_by_name('q')
search.send_keys("python")
search.send_keys(Keys.RETURN)
python=browser.find_element_by_class_name('LC20lb')
python.click()
 
