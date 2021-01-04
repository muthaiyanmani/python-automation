//Automation using python - selenium (LINUX)

1.  sudo apt-get install python //to install python  
            (or)
    sudo apt-get install python3 //to install python3

2.  pip install selenium//to install selenium in python
            (or)
    pip3 install selenium//to install selenium in python3

3.  install webdriver //Eg. Chrome,Firefox,Edge


Program:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#keys provides RETURN,F1,ALT keys etc,.

driver = webdriver.Firefox()
#loaded the webdriver in firefox

driver.get("http://www.python.org")

assert "Python" in driver.title
#it is used to confirm whether the title is correct("Python ") or not

elem = driver.find_element_by_name("q")
elem.clear() #first we will clear for pre populated text

elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source

driver.close() //it closes the one tab
driver.quit() //it closes the entire window

4.Interacting with page

element = send.keys("something",Keys.RETURN)//to write txt and press enter key
element.clear()
#always clear the the contents pre-writtened

#For form filling use Select class
from selenium.webdriver.support.ui import Select
select_by_index(index)


#can also deselect the seleceted the options
select.deselect_all()

#to get all available options
options = Select.options


#once you filled a form use can submit by
driver.find_element_by_id('submit').click()
        (or)
element.submit()

#for Drag and Drop
element = driver.find_element_by_name("source") //here is the source file
target = driver.find_element_by_name("target") //here is ur destination or drop ur file
from selenium.webdriver import ActionChains //to do this drag and drop import this module
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()


#You can also swing from frame to frame (or into iframes):
driver.switch_to_frame("frameName")

#Once we are done with working on frames, we will have to come back to the parent frame which can be done using:
driver.switch_to_default_content()

#pop-up dialogs
alert = driver.switch_to_alert()

#we can move backward and forward our browser history
driver.get('https://google.com')
driver.back()
driver.forward()

#to add a cookie to a particular domain
driver.get("https://web.whatsapp.com")
cookie={'name':" ",'value':" "} //set cookies
driver.add_cookie(cookie) //adding cookies
driver.get_cookies()

4.Locating Elements

find_element_by_id
find_element_by_name
find_element_by_class_name
find_element_by_tag_name
find_element_by_xpath

#using xpath
username = driver.find_element_by_xpath("//form[input/@name='username']")
username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
username = driver.find_element_by_xpath("//input[@name='username']")
#we can also use with two elements
username = driver.find_elements_by_xpath("//input[@name='username'][@type='text']")


#also use partial link text
continue_link = driver.find_element_by_link_text('Continue')
continue_link = driver.find_element_by_partial_link_text('Conti')

5.Waits

i)explicit waits

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait //importing waits
from selenium.webdriver.support import expected_conditions as EC  

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
#using explicit waits
#WebDriverWait calls the ExpectedCondition every 500 milliseconds until it returns success
element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.ID, "myDynamicElement"))
)
finally:
driver.quit()

ii)implicit waits

driver.implicitly_wait(10) # seconds



6.Objects

7.Webdriver API

webdriver.Firefox
webdriver.FirefoxProfile
webdriver.Chrome
webdriver.ChromeOptions
webdriver.Ie
webdriver.Opera
webdriver.PhantomJS
webdriver.Remote
webdriver.DesiredCapabilities
webdriver.ActionChains
webdriver.TouchActions
webdriver.Proxy

Some attributes are callable (or methods) and others are non-callable (properties). All the callable attributes are ending
with round brackets.

Example : driver.current_url //property  , driver.close() //method

The Element Click command could not be completed because the element receiving the events is obscuring the
element that was requested clicked.
//exception selenium.common.exceptions.ElementNotInteractableException
Thrown when an element is present in the DOM but interactions with that element will hit another element do
to paint order
//exception selenium.common.exceptions.ElementNotSelectableException

Thrown when trying to select an unselectable element.
//exception selenium.common.exceptions.ElementNotVisibleException

Thrown when an element is present on the DOM, but it is not visible, and so is not able to be interacted with.
//exception selenium.common.exceptions.ErrorInResponseException









