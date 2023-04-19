#!/usr/bin/env python3

# Script: Ops 401 Class 02 Ops Challenge Solution
# Author: Ethan Brock
# Date of latest revision: 18APR2023
# Purpose: Uptime Sensor Tool
# Resources: Demo, class, Marco
    #REQUIREMENTS
# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# Evaluate the response as either success or failure.
# Assign success or failure to a status variable.
# For every ICMP transmission attempted, print the status variable along with
# a comprehensive timestamp and destination IP tested.
    #DEMO


    # Start Code
# import libraries
import time
import ping3

# functions defined 
ip = "192.168.1.1" # IP address to test
interval = 2 # seconds between pings

while True:
    try:
        response_time = ping3.ping(ip)
        if response_time is not None:
            status = "Network Active"
        else:
            status = "Network Error"
    except:
        status = "Network Error"
    
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")
    print(f"{timestamp} {status} to {ip}")
    
    time.sleep(interval)

    # End Code