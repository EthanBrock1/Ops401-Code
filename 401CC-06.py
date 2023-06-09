#!/usr/bin/env python3

# Script: Ops 401 Class 6 Ops Challenge
# Author:Ethan Brock
# Date of latest revision: 24APR2023
# Purpose: 

    #REQUIREMENTS
#In Python, create a script that utilizes the cryptography library to:

#Prompt the user to select a mode:
#Encrypt a file (mode 1)
#Decrypt a file (mode 2)
#Encrypt a message (mode 3)
#Decrypt a message (mode 4)
#If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
#If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
#Depending on the selection, perform one of the below functions. You’ll need to create four functions:

#Encrypt the target file if in mode 1.
#Delete the existing target file and replace it entirely with the encrypted version.
#Decrypt the target file if in mode 2.
#Delete the encrypted target file and replace it entirely with the decrypted version.
#Encrypt the string if in mode 3.
#Print the ciphertext to the screen.
#Decrypt the string if in mode 4.
#Print the cleartext to the screen.
    #DEMO
# Help from Tyler and ChatGPT

    # Start Code
from cryptography.fernet import Fernet

# Declare Functions
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def display_menu():
    menu = ["1: Encrypt a file", "2: Decrypt a file", "3: Encrypt a message", "4: Decrypt a message", "5: Exit"]
    for i in menu:
        print(i)

def process_file(mode, file_name, key):
    with open(file_name, "rb") as file:
        file_data = file.read()
    fernet = Fernet(key)

    if mode == "1":
        encrypted = fernet.encrypt(file_data)
        with open(file_name, "wb") as file:
            file.write(encrypted)
        return encrypted
    elif mode == "2":
        decrypted = fernet.decrypt(file_data)
        with open(file_name, "wb") as file:
            file.write(decrypted)
        return decrypted

def process_message(mode, message, key):
    fernet = Fernet(key)
    if mode == "3":
        return fernet.encrypt(message.encode('utf-8'))
    elif mode == "4":
        return fernet.decrypt(message.encode('utf-8'))
    
    

# Generate and write a new key
write_key()
key = load_key()

print("Your key is: " + str(key.decode('utf-8')))

while True:
    display_menu()
    mode = input("Please select a mode: ")

    if mode in ["1", "2"]:
        file_name = input("Enter file name: ")
        processed_data = process_file(mode, file_name, key)
        if mode == "1":
            print("Encrypted message is: " + processed_data.decode('utf-8'))
        elif mode == "2":
            print("Decrypted message is: " + processed_data.decode('utf-8'))
    elif mode in ["3", "4"]:
        message = input("Enter message: ")
        processed_data = process_message(mode, message, key)
        if mode == "3":
            print("Encrypted message is: " + processed_data.decode('utf-8'))
        elif mode == "4":
            print("Decrypted message is: " + processed_data.decode('utf-8'))
    elif mode == "5":
        exit()
    # End Code