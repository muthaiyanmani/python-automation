from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
import time


def login_pass(userid,password):
    user = WebDriverWait(browser,50).until(EC.presence_of_element_located((By.XPATH,'//div[@class="_3wU53n"]')))
    user=browser.find_element_by_xpath('//input[@class="_2zrpKA _1dBPDZ"]')
    user.send_keys(userid)
    passwd=browser.find_element_by_xpath('//input[@type="password"]')
    passwd.send_keys(password)
    login=browser.find_element_by_xpath('//button[@class="_2AkmmA _1LctnI _7UHT_c"]')
    login.click()
    time.sleep(2)

def login_otp(otp):
    enter_otp=browser.find_element_by_xpath('//input[@class="_2zrpKA _2Tx0UM"]').send_keys(otp)
    verify=browser.find_element_by_xpath('//button=[@class="_2AkmmA _18ls9P _1eFTEo"]').click()

def add_cart():
    search_item=browser.find_element_by_name('q')
    search_item.send_keys("poco m2 pro")
    search_item.send_keys(Keys.RETURN)
    select_item = WebDriverWait(browser,50).until(EC.presence_of_element_located((By.XPATH,'//div[@class="_3wU53n"]')))
    select_item.click()
    add_cart=select_item = WebDriverWait(browser,50).until(EC.presence_of_element_located((By.XPATH,'//button[@class="_2AkmmA _2Npkh4 _2MWPVK"]')))
    add_cart.click()


choice=int(input(" 1.SignIn with Password \t2.SignIn with OTP\n \n Enter your choice: "))

if choice==1:
    userid=input(" \n Enter email/mobile no: ")
    password=getpass("\n Enter password: ")
    browser=webdriver.Chrome('/home/mumu/Documents/Automation/chromedriver')
    browser.maximize_window()
    browser.get('http://www.google.com')
    search=browser.find_element_by_name('q')
    search.send_keys("flipkart")
    search.send_keys(Keys.RETURN)
    select=browser.find_element_by_class_name('LC20lb')
    select.click()
    time.sleep(3)
    login_pass(userid,password)
    add_cart()



elif choice==2:
    userid=input("\n Enter Mobile no: ")  
    browse()
    user=browser.find_element_by_xpath('//input[@class="_2zrpKA _1dBPDZ"]')
    user.send_keys(userid)
    req_otp=browser.find_element_by_xpath('//button[@class="_2AkmmA _1LctnI jUwFiZ"]').click()
    otp=int(input("Enter OTP: "))



else:
    print("Enter correct choice!")



