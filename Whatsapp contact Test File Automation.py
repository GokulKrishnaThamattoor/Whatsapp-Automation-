from selenium import webdriver #importing the selenium
import time      #importing the time from Python

chrome=webdriver.Chrome('chromedriver.exe')#Calling The Selenium Webdriver Application
#Note:Either Keep the selenium ChromeDriver.Exe File In Same File where The Program is Stored Else ctrl+C the Path where you have Stired the ChromeDriver.exe
chrome.get('http://web.whatsapp.com')#Calling The Whatsapp Web From the Browser
chrome.maximize_window()#Use to Maximize the window of whatsapp web if its small
input('Enter any key after QR scan')#Asking User to Scan the qrcode and Press Enter in this Screen if u have scanned
chrome.implicitly_wait(2)#juz waiting for 2 Seconds
message=input("Enter the Message")#getting message from user
print (message) #printing tjhe message
fileread = open("ContactFile.txt", "r") #storing the contacts in a text file
for i in fileread:
    chrome.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys("Search Contact") #used to search a contact from list(Search Contact inside send key pls add the contact to be searched)
    user = chrome.find_element_by_xpath('//span[@title="' +i.strip()+ '"]')#used to strip blankspaces
    print("contact", i) #printing the Contacts
    chrome.implicitly_wait(1) #waiting
    user.click() #Click
    msgbox=chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message) #msg area
    button=chrome.find_element_by_class_name('_35EW6') # send button
    button.click() #the Button Click
    chrome.implicitly_wait(1) #the Browser wait
time.sleep(15) #browser Sleeping time
chrome.close() #Closing the browser automatically
print('Completed')