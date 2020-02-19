from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By

Time = "3:00"

with open("string.txt" , 'r') as file:
    pswd = file.read()
lookup = Time

with open("PremierVariables.txt") as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            print ('found at line:', num)
# browser = webdriver.Chrome(executable_path=r'C:\Users\Administrator\AppData\Local\chromedriver_win32\chromedriver.exe')
# browser.get('https://sso.premierinc.com/login')
# username = browser.find_element_by_id("username")
# username.send_keys("armando.villegas@mssm.edu")
# password = browser.find_element_by_id("password")
# password.send_keys(pswd)
# #browser.execute_script("document.getElementById('login-button').click()")
# browser.implicitly_wait(5)
# browser.execute_script("document.getElementsByClassName('ss-card-name')[2].click()") #Click OperationsAdvisor and SupplyFocus
# browser.implicitly_wait(15)
# NewWindow = browser.window_handles[1]
# browser.switch_to.window(NewWindow)
# j=0
# Test = "centerFrame.contentDocument.getElementsByClassName('tabLabel')[2].click()"#Click on Publishing
# browser.execute_script(Test)
# 
# time.sleep(20)
# ValidCount = browser.execute_script("return centerFrame.contentDocument.getElementsByClassName('dgrid-content ui-widget-content')[2].getElementsByTagName('a').length") #Get number of "Start Data Validation" on page
# for i in range(1, ValidCount+1):
#     EntityName = "return centerFrame.contentDocument.getElementsByClassName('dgrid-cell dgrid-cell-padding dgrid-column-0 field-entityName')[%s].textContent" %(str(i))
#     PrintEntity = browser.execute_script(EntityName)
#     print(PrintEntity)
#    # print(i)
#     if PrintEntity.find("Beth Israel") != -1:
#       j=j+1
#       print(j)
#       #StartValid = "centerFrame.contentDocument.getElementsByClassName('dgrid-cell dgrid-cell-padding dgrid-column-4 field-statusTxt')[%s].getElementsByTagName('a')[0].click()" %(str(i))
#       #execute_script(StartValid) #Click on first "Start Data Validation" 
#       #browser.execute_script("centerFrame.contentDocument.getElementById('nextBtn_label').click()") #Click on "Continue Publishing Data"
#       #time.sleep(10)
#       #browser.execute_script("centerFrame.contentDocument.getElementById('ap-deselect-all-0').click()") #Deselect whole last column
#       #time.sleep(1)
#       #browser.execute_script("centerFrame.contentDocument.getElementById('nextBtn_label').click()") #Click on "Continue Publishing Data"
#       #time.sleep(5)
#       #browser.execute_script("centerFrame.contentDocument.getElementsByClassName('dijitReset dijitCheckBoxInput')[1].click()") #Click on middle bullet
#       #time.sleep(1)
#       #browser.execute_script("centerFrame.contentDocument.getElementById('cancelLink').click()") #Click Cancel
#       #time.sleep(5)
#       #browser.execute_script("centerFrame.contentDocument.getElementById('doneBtn_label').click()") #Click on "Complete Publishing Data"
#       #time.sleep(5)
# browser.quit()
