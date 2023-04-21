#!/usr/bin/env python3

# Script: Ops 401 Class 03 Ops Challenge Solution
# Date of latest revision: 19APR2023
# Credit to Tyler for walking me through this to help me catch up

    #REQUIREMENTS

    #DEMO
# import libraries
#import smtplib
#import datetime, time, os
#from getpass import getpass

# Test email functionality
#password = getpass("Please provide your password")

# Ctreate SMTP session
#s = smtplib.SMTP('smtp.gmail.com', 587)

# Start TLS for security
#s.starttls()

# Authentication
#s.login(email, password)

# Message to be sent
#s.sendmail(heartbeat@bot.com)

# Declare Variable
#up = "Network is active"
#down = "Network is down"
#email = input("Please provide your email address:")
#password = getpass("Please provide your password:")
#ip = input("Provide an IP address you would like to monitor:")
#last = 0
#ping_result = 0


    # Declare Functions

# Function to handle the up alert
#def send_upAlert():
#    now = datetime.datetime.now()
#    s = smtplib.SMTP('smtp.gmail.com', 587)
#    s.starttls()
#    s.login(email,password)
#    message = "your server came back to life"
#    s.sendmail("heartbeat@bot.com", email, message)
#    s.quit()

# Function that handles the down alert
#def send_downAlert():

# Function that does the ping test
#def ping_test():

#    if ((ping_result != last) and (ping_result == up)):
#        last = up
#        send_upAlert()
#    elif ((ping_result != last) and (ping_result == down)):
#        send_downAlert()
#        last = down

#    response = os.system("ping .c +1 " + ip)
#    if response == 0:
#        ping_result = up
#    else:
#        ping_result = down


# Infinite loop
#while True:
#    ping_test()
#    time.sleep(2)
#break 
    # Start Code
 #Import libraries
import os, time, smtplib 
from datetime import datetime
from getpass import getpass 

#prompts for email to use for notifications.

currentTime = datetime.now()
up = 0
down = 1
last = 0
email = input("Please enter your email address\n")
pw = getpass("Please enter the password\n")
#asks user for input of ip address
IP = input("Please enter an IP address\n")
print("\n")
def send_downmessage():
    #create SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(email, pw)
    # Message 
    message = ("Subject: Python script\n\nYour server is not serving " + currentTime)
    s.sendmail("Heartbeat@bot.com",email, message)
    # Terminate Session
    s.quit()

def send_upmessage():
    
    #create SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(email, pw)
    # Message 
    message = ("Subject: Python script\n\n\Your server is serving " + currentTime)
    s.sendmail("Heartbeat@bot.com",email, message)
    # Terminate Session
    s.quit()

def ping_test(): 
    global last
    ping_result = os.system("ping -c 1 " + IP)
        #Check if host is up or down
    if  ((ping_result != last) and (ping_result == up)):
        last = up
        send_upmessage()
    elif ((ping_result != last) and (ping_result == down)):
        last = down
        send_downmessage()

#Infinite loops to keep pinging target
while True:
#creates function for ping and status 
    ping_test
    time.sleep(2)
 break
    # End Code