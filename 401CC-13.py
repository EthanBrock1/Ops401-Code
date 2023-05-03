#!/usr/bin/env python3

# Script: Ops 401 Class 13 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 
# Purpose: 
# Credit: Me and Chatgpt
    #REQUIREMENTS
#In Python, combine the two modes (port and ping) of your network scanner script.
#Eliminate the choice of mode selection.
#Continue to prompt the user for an IP address to target.
#Move port scan to its own function.
#Call the port scan function if the host is responsive to ICMP echo requests.
#Print the output to the screen.
    #DEMO


    # Start Code
import ipaddress
from scapy.all import IP, TCP, sr1, ICMP

# Define port range or specific set of ports to scan
PORT_RANGE = [22, 23, 80, 443, 3389]

def port_scan(host):
    """Scan a host for open ports in the specified port range."""
    open_ports = []
    for dst_port in PORT_RANGE:
        src_port = 1025
        response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="S"), timeout=1, verbose=0)
        if(response is not None):
            if(response.haslayer(TCP)):
                # If flag 0x12 received, send a RST packet to graciously close the open connection.
                # Notify the user the port is open.
                if(response.getlayer(TCP).flags == 0x12):
                    send_rst = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="R"), timeout=1, verbose=0)
                    open_ports.append(dst_port)
                # If flag 0x14 received, notify user the port is closed.
                elif(response.getlayer(TCP).flags == 0x14):
                    pass
            # If no flag is received, notify the user the port is filtered and silently dropped.
            else:
                pass
    return open_ports

# Prompt user for IP address to target
ip_address = input("Enter an IP address to target: ")

# Ping the host to see if it's online
response = sr1(IP(dst=ip_address)/ICMP(), timeout=1, verbose=0)
if response is None:
    print(ip_address, "is down or unresponsive")
else:
    open_ports = port_scan(ip_address)
    if len(open_ports) > 0:
        print(ip_address, "is up and has the following open ports:", open_ports)
    else:
        print(ip_address, "is up but has no open ports")

    # End Code