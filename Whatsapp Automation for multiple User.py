from selenium import webdriver  #Importing The Selenium Web Driver
import time                     #Importing The Time Function In Python

chrome=webdriver.Chrome('chromedriver.exe')   #Calling The Selenium Webdriver Application
#Note:Either Keep the selenium ChromeDriver.Exe File In Same File where The Program is Stored Else ctrl+C the Path where you have Stired the ChromeDriver.exe
chrome.get('http://web.whatsapp.com') #Calling The Whatsapp Web From the Browser
chrome.maximize_window()  #Use to Maximize the window of whatsapp web if its small
input('Enter any key after QR scan') #Asking User to Scan the qrcode and Press Enter in this Screen if u have scanned

chrome.implicitly_wait(2)  #juz waiting for 2 Seconds

ContactBucket = []  #Getting Multiple Contacts in List(Currently Test & Notepad are my contact)
ContactBucket = input("Enter the Contacts and while adding next contact memeber pls add coma between ")#getting the contacts from user and while getting next contact pls add comma
ContactBucket  = ContactBucket.split(",")#the Contact splliter
for Contacts in ContactBucket: #getting Contacts in Contact Bucket
    print(Contacts) #printing the Contact
message=input("Enter the Message pls:")   #The Message area
print("message is",message)
for i in ContactBucket:                  #Loop Area for getting Valuse in List as input
    user = chrome.find_element_by_xpath('//span[@title="' + i + '"]')  #used Xpath for getting the location
    print("contact", i)    #printing the Contacts Gien in the List
    chrome.implicitly_wait(1) #Waiting 1 Sec
    user.click() #The Click Button
    msgbox=chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message) #msg area
    button=chrome.find_element_by_class_name('_35EW6') # send button
    button.click() #Button Clicking
    #.implicitly_wait(1)

#browser.implicitly_wait(15)
time.sleep(15)  #Sleep time For Browser like a Wait
chrome.close()  #Closing The Browser
print('Completed')