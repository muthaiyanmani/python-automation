from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

emailid=input("Enter your Email: ")
password=input("Enter your password: ")

driver=webdriver.Chrome(executable_path='/home/mumu/Documents/Automation/chromedriver')
driver.maximize_window()
driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
driver.find_element_by_xpath('//button[@data-provider="google"]').click()
#signing in
mail=driver.find_element_by_xpath("//input[@type='email']")
mail.send_keys(emailid)
time.sleep(3)
mail.send_keys(Keys.RETURN)
#passwd = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.NAME, "password")))
passwd=driver.find_element_by_xpath("//input[@name='password']")
time.sleep(1)
passwd.send_keys(password)
time.sleep(3)
passwd.send_keys(Keys.RETURN)


#driver.get('https://www.youtube.com')
# search=driver.find_element_by_name('search_query') instead of next
# using explicit wait
search = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.NAME, "search_query")))
search.send_keys("react js mosh")
search.send_keys(Keys.RETURN)
select=driver.find_element_by_xpath('//yt-formatted-string[@class="style-scope ytd-video-renderer"]')
select.click()
time.sleep(3)
signin=driver.find_element_by_xpath("//yt-formatted-string[@class='style-scope ytd-button-renderer style-suggestive size-small']").click()

time.sleep(5)
nextButton = driver.find_element_by_id('next')
nextButton.click()



# time.sleep(1)
# email.send_keys(Keys.RETURN)


