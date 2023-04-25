#!/usr/bin/env python3

# Script: Ops 401 Class 7 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 25APR2023
# Purpose: 

    #REQUIREMENTS
#Add a feature capability to your script to:

#Recursively encrypt a single folder and all its contents.
#Recursively decrypt a single folder that was encrypted by this tool.
    #DEMO


    # Start Code
import os
from cryptography.fernet import Fernet

# Declare Functions
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def display_menu():
    menu = ["1: Encrypt a file", "2: Decrypt a file", "3: Encrypt a message", "4: Decrypt a message", "5: Encrypt a folder", "6: Decrypt a folder", "7: Exit"]
    for i in menu:
        print(i)

def process_file(mode, file_path, key):
    with open(file_path, "rb") as file:
        file_data = file.read()
    fernet = Fernet(key)

    if mode == "1":
        encrypted = fernet.encrypt(file_data)
        with open(file_path, "wb") as file:
            file.write(encrypted)
        return encrypted
    elif mode == "2":
        decrypted = fernet.decrypt(file_data)
        with open(file_path, "wb") as file:
            file.write(decrypted)
        return decrypted

def process_message(mode, message, key):
    fernet = Fernet(key)
    if mode == "3":
        return fernet.encrypt(message.encode('utf-8'))
    elif mode == "4":
        return fernet.decrypt(message.encode('utf-8'))

def process_folder(mode, folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            process_file(mode, file_path, key)

# Generate and write a new key
write_key()
key = load_key()

print("Your key is: " + str(key.decode('utf-8')))

while True:
    display_menu()
    mode = input("Please select a mode: ")

    if mode in ["1", "2"]:
        file_path = input("Enter file path: ")
        processed_data = process_file(mode, file_path, key)
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
        folder_path = input("Enter folder path: ")
        process_folder("1", folder_path, key)
        print("Folder encrypted successfully!")
    elif mode == "6":
        folder_path = input("Enter folder path: ")
        process_folder("2", folder_path, key)
        print("Folder decrypted successfully!")
    elif mode == "7":
        exit()

    # End Code