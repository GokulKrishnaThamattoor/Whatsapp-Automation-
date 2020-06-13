from selenium import webdriver #Importing The Selenium Web Driver
import time                    #Importing The Time Function In Python
chrome=webdriver.Chrome('chromedriver.exe')#Calling The Selenium Webdriver Application
#Note:Either Keep the selenium ChromeDriver.Exe File In Same File where The Program is Stored Else ctrl+C the Path where you have Stired the ChromeDriver.exe
chrome.get('http://web.whatsapp.com') #Calling The Whatsapp Web From the Browser
chrome.maximize_window() #Use to Maximize the window of whatsapp web if its small
input('Enter any key after QR scan')#Asking User to Scan the qrcode and Press Enter in this Screen if u have scanned
chrome.implicitly_wait(4) #juz waiting for 4 Seconds
Tell=input("Enter the Person Name:")#Getting the person
user=chrome.find_element_by_xpath('//span[@title="'+Tell+'"]')#used Xpath for getting the location
user.click() #The Click Button
message=input("Enter the Message")#Getting the req message needed to send
print("Message is",message) #printing the Messag
n=int(input("Enter the total no of times needed to send the msg"))
count=n#How many times needed to Send the message
for i in range(count): #Looping the message
    msgbox=chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message) #msg area
    button=chrome.find_element_by_class_name('_35EW6') # send button
    button.click() #Send Button Clicking
    #time.sleep(15)  # Sleep time For Browser like a Wait
   # chrome.close()  # Closing The Browser

print('Completed')
