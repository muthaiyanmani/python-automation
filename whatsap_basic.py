from selenium import webdriver
browser=webdriver.Chrome(executable_path='\chromedriver.exe')
browser.get('http://web.whatsapp.com')
name=input("Enter the name:\t")

user=browser.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()
msg="Sorry :("
count=int(input("Enter the counts limit: "))
msgbox=browser.find_element_by_xpath("//div[@spellcheck='true']")

for i in range(count):
    msgbox.send_keys(msg)
    button=browser.find_element_by_class_name('_1U1xa')
    button.click()
print ("completed")


 
