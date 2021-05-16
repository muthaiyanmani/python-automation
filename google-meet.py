from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import time,ctime,sleep
import getpass
from datetime import datetime 


def welcome():
    print("\n@@@@@@ G - Meet b0t Welcomes you! @@@@@")
    t = time()
    print("\nCurrent time:",ctime(t),"\n")
    print("\n######### ReadME #######\n")
    print("1.Make sure that your e-mail has two factor authentication turned off")
    print("2.You may enter class timing 1 hour before .it will automatically joined")
    print("3.If any error occurs ,restart me\n")

def mail_password_validation():
    email=input("Enter your e-mail address: ")
    password = getpass.getpass(prompt='Enter your password: ')
    print("\n###### e-mail and password has been received from user. ######\n")
    return email,password
    

def link_validation():
    valid_link = 1
    while(valid_link):
        link=input("Paste your google meet link here : ")
        link_length = len(link)

        if(link_length==12):
            temp_link = "https://meet.google.com/"
            final_link = "".join([temp_link, link])
            valid_link=0
        elif(link_length==28 or link_length==29):
            temp_link = "https://"
            final_link = "".join([temp_link, link])
            valid_link = 0
        elif(link_length==36 or link_length==37):
            final_link = link
            valid_link = 0
        else:
            print("\nInvalid link. try again..\n")
            valid_link = 1
    print("\n###### Your link has been verified. #######\n")
    return final_link

def time_validation():
    valid_time = 1
    while(valid_time):
        final_time=int(input("\nEnter your class timing here : (HHMM 24-hour format) "))
        if(final_time<=2359):
            valid_time=0
        else:
            print("\nInvalid time..\n")
            valid_time = 1
    print("\n###### Your class timing has been valid. #######")
    return final_time


welcome()
email,password = mail_password_validation()
final_link = link_validation()  
final_time = time_validation()

print("\n############ Waiting for time. ##########\n")

while(True):
    now=datetime.now()
    str_time=now.strftime("%H%M")
    current_time=int(str_time)

    if(current_time+3<=final_time):
        break
    sleep(50)
    

# create chrome instamce
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
# driver = webdriver.Chrome(executable_path=r'C:\Users\Muthaiyan Mani\Documents\Automation\chromedriver')
driver = webdriver.Chrome(options=opt)
  
def login(mail_address, password,final_link):
        
    driver.get(
            'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
  
    # input Gmail
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(10)
  
    # input Password
    driver.find_element_by_xpath(
            '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element_by_id("passwordNext").click()
    driver.implicitly_wait(100)
    
    # go to google home page
    driver.get('https://google.com/')
    driver.implicitly_wait(200)
    sleep(5)
    driver.get(final_link)
    driver.implicitly_wait(50)
    print("\n####### login successfull. ######\n")
  
  
def turn_off_mic_cam():
    # turn off Microphone
    driver.implicitly_wait(3000)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    driver.implicitly_wait(3000)
    
    # turn off camera
    driver.implicitly_wait(100)
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div").click()
    driver.implicitly_wait(3000)
    print("Turnedd Off")
      
      
def join_now():
    # Join meet
    sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    print(1)
  
  
def ask_to_join():
    # Ask to Join meet
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    # Ask to join and join now buttons have same xpaths
      
# login to Google account
login(email, password,final_link)
  
# go to google meet
turn_off_mic_cam()
# AskToJoin()
join_now()