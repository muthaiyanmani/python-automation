from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from csv import reader
from time import sleep

# Getting Contacts and Contact Names from csv file and store it in dictionary
all_contacts = {}
with open('contacts.csv', "r") as f:
    csv_reader = reader(f)
    for row in csv_reader:
        all_contacts[row[1]] = row[0]

# Target Contact Numbers
target_mobiles = all_contacts.keys()

# Target Contact Names
target_names = all_contacts.values()

# Store session in local (UBUNTU)
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=.config/google-chrome/Default')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open whatsapp web
driver.get('https://web.whatsapp.com/')
sleep(8)

# Getting input for sending message or file
choice = int(input(
    "Enter options:\n 1. Send Message\n 2. Send File or Audio or Video\n Note: Enter 1 or 2 \n"))

# Sending message to all contacts
if choice == 1:

    # Getting input of message
    message = input("Enter message : ")

    # Send message to all targets
    for target_mobile in target_mobiles:

        # Checking group or mobile number
        if(target_mobile[0:8] == "https://"):
            invitation = target_mobile[26:]
            driver.get("https://web.whatsapp.com/accept?code="+invitation)
            sleep(8)
        elif target_mobile.isdigit():
            driver.get("https://web.whatsapp.com/send?phone=91"+target_mobile)  # +"&text="+message
            sleep(8)

        else:
            search_box = driver.find_element_by_xpath(
                "//div[@contenteditable='true']")
            sleep(2)
            search_box.click()
            sleep(2)
            search_box.send_keys(target_mobile)
            sleep(7)
            target = driver.find_element_by_xpath(
                "//span[@class='matched-text _3Whw5']")
            sleep(2)
            target.click()
            sleep(2)

        try:
            # Finding message box
            msg_box = driver.find_element_by_xpath("//div[@spellcheck='true']")
            msg_box.click()
            sleep(5)
        except:
            print(all_contacts[target_mobile], 'gives invalid contact')
            continue

        # Put message to message box
        msg_box.send_keys(message)
        sleep(3)
        # Press ENTER for sendind a message
        msg_box.send_keys(Keys.ENTER)
        print(message, 'sent successfully to', all_contacts[target_mobile])
        sleep(5)

    print(message, 'sent successfully to all.\n \t\tThank you!')

# Sending file to all contacts
elif choice == 2:

    # Getting input of filepath
    filepath = input("Enter filepath : ")

    # Send file to all targets
    for target_mobile in target_mobiles:

        # Checking group or mobile number
        if(target_mobile[0:8] == "https://"):
            invitation = target_mobile[26:]
            driver.get("https://web.whatsapp.com/accept?code="+invitation)
            sleep(8)

        elif target_mobile.isdigit():
            driver.get("https://web.whatsapp.com/send?phone=91" +
                       target_mobile)  # +"&text="+message
            sleep(8)

        else:
            search_box = driver.find_element_by_xpath(
                "//div[@contenteditable='true']")
            sleep(2)
            search_box.click()
            sleep(2)
            search_box.send_keys(target_mobile)
            sleep(7)
            target = driver.find_element_by_xpath(
                "//span[@class='matched-text _3Whw5']")
            sleep(2)
            target.click()
            sleep(2)

        try:
            # Finding attachments button
            driver.find_element_by_xpath("//div[@title='Attach']").click()
            sleep(5)
        except:
            print(all_contacts[target_mobile], 'gives invalid contact')
            continue

        # Pass filepath to the attachment
        attach = driver.find_element_by_xpath(
            "//input[@accept='*']")
        try:
            attach.send_keys(filepath)
            sleep(3)
        except:
            print("File not found")
            break

        # Sendind attachment to the target
        driver.find_element_by_xpath("//span[@data-icon='send']").click()
        sleep(3)

        # To remove the control from attachment
        driver.find_element_by_xpath(
            "//div[@aria-label='Message list. Press right arrow key on a message to open message context menu.']").click()

        print(filepath, 'sent successfully to', all_contacts[target_mobile])
        sleep(5)

    print(filepath, 'sent successfully to all.\n \t\tThank you!')

else:
    print("Wrong choice")

# /home/sakthivel/Downloads/20200613_18707_0000.png - File not found
# /home/sakthivel/Downloads/cloud-introduction.pptx
# /home/sakthivel/Downloads/20200613_110707_0000.png
