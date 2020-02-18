from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By

with open("string.txt" , 'r') as file:
    pswd = file.read()
browser = webdriver.Chrome(executable_path=r'C:\Users\Administrator\AppData\Local\chromedriver_win32\chromedriver.exe')
browser.get('https://sso.premierinc.com/login')
username = browser.find_element_by_id("username")
username.send_keys("armando.villegas@mssm.edu")
password = browser.find_element_by_id("password")
password.send_keys(pswd)
#browser.execute_script("document.getElementById('login-button').click()")
browser.implicitly_wait(5)
browser.execute_script("document.getElementsByClassName('ss-card-name')[2].click()") #Click OperationsAdvisor and SupplyFocus
browser.implicitly_wait(15)
NewWindow = browser.window_handles[1]
browser.switch_to.window(NewWindow)
browser.execute_script("centerFrame.contentDocument.getElementsByClassName('tabLabel')[2].click()") #Click on Publishing
time.sleep(10)
ValidCount = browser.execute_script("return centerFrame.contentDocument.getElementsByClassName('dgrid-content ui-widget-content')[2].getElementsByTagName('a').length") #Get number of "Start Data Validation" on page
for i in range(1, ValidCount+1):
    browser.execute_script("centerFrame.contentDocument.getElementsByClassName('dgrid-cell dgrid-cell-padding dgrid-column-4 field-statusTxt')[1].getElementsByTagName('a')[0].click()") #Click on first "Start Data Validation" 
    time.sleep(5)
    browser.execute_script("centerFrame.contentDocument.getElementById('nextBtn_label').click()") #Click on "Continue Publishing Data"
    time.sleep(10)
    browser.execute_script("centerFrame.contentDocument.getElementById('ap-deselect-all-0').click()") #Deselect whole last column
    time.sleep(1)
    browser.execute_script("centerFrame.contentDocument.getElementById('nextBtn_label').click()") #Click on "Continue Publishing Data"
    time.sleep(5)
    browser.execute_script("centerFrame.contentDocument.getElementsByClassName('dijitReset dijitCheckBoxInput')[1].click()") #Click on middle bullet
    time.sleep(1)
    browser.execute_script("centerFrame.contentDocument.getElementById('cancelLink').click()") #Click Cancel
    #browser.execute_script("centerFrame.contentDocument.getElementById('doneBtn_label').click()") #Click on "Complete Publishing Data"
    time.sleep(5)
    
browser.quit()
