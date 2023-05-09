#!/usr/bin/env python3

# Script: Ops 401 Class 16 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 08MAY2023
# Purpose: brute force attack
# Resources: Chatgpt
    #REQUIREMENTS
#In Python, create a script that prompts the user to select one of the following modes:

#Mode 1: Offensive; Dictionary Iterator

#Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
#Add a delay between words.
#Print to the screen the value of the variable.

#Mode 2: Defensive; Password Recognized

#Accepts a user input string.
#Accepts a user input word list file path.
#Search the word list for the user input string.
#Print to the screen whether the string appeared in the word list.
    #DEMO


    # Start Code
import time

print("Select a mode:")
print("1. Offensive; Dictionary Iterator")
print("2. Defensive; Password Recognized")

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
else:
    print("Invalid mode selected.")
    # End Code