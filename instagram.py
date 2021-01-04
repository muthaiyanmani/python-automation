from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from csv import reader
from time import sleep

followid=input("Enter id whom you want to follow: ")
print("\n\n")

# take an empty dictionary
credentials_list={}
with open ('credentials.csv',"r") as f:
    credential_read=reader(f)
    for row in credential_read:
        credentials_list[row[1]] = row[0]


# now stored all credentials
userid=credentials_list.keys()
passwd=credentials_list.values()



def browse(userid,passwd):
    browser=webdriver.Chrome('/home/mumu/Documents/Automation/chromedriver')
    browser.maximize_window()
    browser.get('http://www.instagram.com')
    # implicit wait
    usrid = WebDriverWait(browser,50).until(EC.presence_of_element_located((By.XPATH,'//div[@class="_3wU53n"]')))
    usrid.send_keys(userid)
    paswd = WebDriverWait(browser,50).until(EC.presence_of_element_located((By.XPATH,'//div[@class="_3wU53n"]')))
    paswd.send_keys(passwd)
    paswd.send_keys(Keys.RETURN)

def find_follow(followid):
    search = WebDriverWait(browser,50).until(EC.presence_of_element_located((By.XPATH,'//div[@class="_3wU53n"]')))
    search.send_keys(followid)
    # follow that id
    follow = WebDriverWait(browser,50).until(EC.presence_of_element_located((By.XPATH,'//div[@class="_3wU53n"]')))
    follow.click()



browse(userid,passwd)
find_follow(followid)
browser.quit()



