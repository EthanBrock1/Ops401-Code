#!/usr/bin/env python3

# Script: Ops 401 Class 8 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 26APR2023
# Purpose: 
# Resources: Tyler and ChatGPT  
    #REQUIREMENTS
#Add a feature capability to your Python encryption tool to:

#Alter the desktop wallpaper on a Windows PC with a ransomware message
#Create a popup window on a Windows PC with a ransomware message
#Make this feature optional. In the user menu prompt, add this as a ransomware simulation option.
    #DEMO

### NOT FINISHED
    # Start Code
import os
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
from PIL import Image, ImageDraw, ImageFont

# Declare Functions

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def display_menu():
    menu = ["1: Encrypt a file", "2: Decrypt a file", "3: Encrypt a message", "4: Decrypt a message", "5: Ransomware simulation", "6: Exit"]
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

def ransomware_sim():
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Ransomware Alert", "Your computer has been infected with ransomware! Please pay $500 to unlock your files.")

    bg_color = (0, 0, 0)
    text_color = (255, 255, 255)
    im = Image.new(mode = "RGB", size = (1920, 1080), color = bg_color)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 60)
    draw.text((500, 500), "Your computer has been locked!", fill = text_color, font = font)
    im.save("ransomware_wallpaper.jpg")
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath("ransomware_wallpaper.jpg"), 0)

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
        ransomware_sim()
    elif mode == "6":


    # End Code
