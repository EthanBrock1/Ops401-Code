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
#ChatGPT
from cryptography.fernet import Fernet
import os

def encrypt_file(key, filename):
    with open(filename, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(filename, 'wb') as f:
        f.write(encrypted)

def decrypt_file(key, filename):
    with open(filename, 'rb') as f:
        encrypted = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted)
    with open(filename, 'wb') as f:
        f.write(decrypted)

def encrypt_message(key, message):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    print(encrypted.decode())

def decrypt_message(key, message):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(message.encode())
    print(decrypted.decode())

def main():
    key = Fernet.generate_key()
    print("Welcome to the encryption tool!")
    print("Please select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    mode = int(input("> "))
    if mode == 1:
        filename = input("Please enter the filepath of the file to encrypt: ")
        encrypt_file(key, filename)
        print("File encrypted!")
    elif mode == 2:
        filename = input("Please enter the filepath of the file to decrypt: ")
        decrypt_file(key, filename)
        print("File decrypted!")
    elif mode == 3:
        message = input("Please enter the message to encrypt: ")
        encrypt_message(key, message)
    elif mode == 4:
        message = input("Please enter the message to decrypt: ")
        decrypt_message(key, message)
    else:
        print("Invalid mode selected.")

if __name__ == '__main__':
    main()


    # Start Code

    # End Code