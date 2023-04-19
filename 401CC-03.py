#!/usr/bin/env python3

# Script: Ops 401 Class 03 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 19APR2023
# Purpose: 

    #REQUIREMENTS

    #DEMO
# import libraries
import smtplib
import datetime, time, os
from getpass import getpass

# Test email functionality
password = getpass("Please provide your password")

# Ctreate SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# Start TLS for security
s.starttls()

# Authentication
s.login(email, password)

# Message to be sent
s.sendmail(heartbeat@bot.com)

    # Start Code

# Declare Variable
up = "Network is active"
down = "Network is down"
email = input("Please provide your email address:")
password = getpass("Please provide your password:")
ip = input("Provide an IP address you would like to monitor:")
last = 0
ping_result = 0


    # Declare Functions

# Function to handle the up alert
def send_upAlert():
    now = datetime.datetime.now()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email,password)
    message = "your server came back to life"
    s.sendmail("heartbeat@bot.com", email, message)
    s.quit()

# Function that handles the down alert
def send_downAlert():

# Function that does the ping test
def ping_test():

    if ((ping_result != last) and (ping_result == up)):
        last = up
        send_upAlert()
    elif ((ping_result != last) and (ping_result == down)):
        send_downAlert()
        last = down

    response = os.system("ping .c +1 " + ip)
    if response == 0:
        ping_result = up
    else:
        ping_result = down


# Infinite loop
while True:
    ping_test()
    time.sleep(2)
break 

 
    # End Code