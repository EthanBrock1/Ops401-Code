#!/usr/bin/env python3

# Script: Ops 401 Class 12 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 02MAY2023
# Purpose: Network Security Tool

    #REQUIREMENTS
#Add the following features to your Network Security Tool:

#User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set
#ICMP Ping Sweep tool
#Prompt user for network address including CIDR block, for example “10.10.0.0/24”
#Careful not to populate the host bits!

#Create a list of all addresses in the given network
#Ping all addresses on the given network except for network address and broadcast address
#If no response, inform the user that the host is down or unresponsive.
#If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
#Otherwise, inform the user that the host is responding.
#Count how many hosts are online and inform the user.
    #DEMO
# ----- ICMP Ping Sweep tool -----
#from scapy.all import ICMP, IP, sr1, TCP
#import ipaddress
# Python's ipaddress module which provides the ability to create, manipulate and operate on IPv4 and IPv6 addresses and networks. This is included with Python 3.3+, so you do not need to install it.

# Declare Variables
#ip = "127.0.0.1"
#myIp = "10.0.0.68"
#host = "scanme.nmap.org"
#network = '10.0.0.1/24'

# ----- Initialize an IPv4Address! -----
# ip4 = ipaddress.IPv4Address(ip)
# print(ip4.is_multicast)
  # Print True if the IP address is a loopback address.
# print("Is loopback: ", ip4.is_loopback)

# ----- Initialize an IPv4Network() -----
#ip4Network = ipaddress.IPv4Network("192.168.1.0/24")
# Print the network address of the network.
#print("Network address of the network: ", ip4Network.network_address)

  # Print the broadcast address
#print("Broadcast address: ", ip4Network.broadcast_address)

  # Print the network mask.
#print("Network mask: ", ip4Network.netmask)


#response = sr1(IP(dst=host)/ICMP(), timeout=1, verbose=0)

# If the response is empty, then the host is down
#if response is None:
#  print("Host down")
# Check for ICMP codes
#  if response.haslayer(ICMP):
#    response.getlayer(ICMP).code # now compare the reutnred code to 1, 2, 3, 9, 10, or 13.
      # Then the host is actively blocking ICMP traffic.
      # How do you cast to Integer in Python? String ->(cast) Integer "2" X 2 => int("2")
# if no codes and reponse is good, host is up and responding! sebnd a RST(reset)

    # Start Code
import os
import ipaddress
from scapy.all import sr1, ICMP

# User menu
print("Welcome to the Network Security Tool")
print("1. TCP Port Range Scanner mode")
print("2. ICMP Ping Sweep mode")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    # TCP Port Range Scanner mode
    # Utilize the scapy library
    from scapy.all import IP, sr1, TCP

    # Define host IP
    host = "scanme.nmap.org"

    # Define port range or specific set of ports to scan
    port_range = [22, 23, 80, 443, 3389]

    # Test each port in the specified range using a for loop
    for dst_port in port_range:
        src_port = 1025
        response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port,flags="S"), timeout=1, verbose=0)
        if(response is not None):
            if(response.haslayer(TCP)):
                # If flag 0x12 received, send a RST packet to graciously close the open connection.
                # Notify the user the port is open.
                if(response.getlayer(TCP).flags == 0x12):
                    send_rst = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="R"), timeout=1, verbose=0)
                    print("Port", dst_port, "is open")
                # If flag 0x14 received, notify user the port is closed.
                elif(response.getlayer(TCP).flags == 0x14):
                    print("Port", dst_port, "is closed")
            # If no flag is received, notify the user the port is filtered and silently dropped.
            else:
                print("Port", dst_port, "is filtered and dropped")

elif choice == "2":
    # ICMP Ping Sweep mode
    # Prompt user for network address including CIDR block
    network_addr = input("Enter network address with CIDR block (e.g. 10.10.0.0/24): ")

    # Create a list of all addresses in the given network
    network = ipaddress.ip_network(network_addr, strict=False)
    hosts = list(network.hosts())

    # Ping all addresses on the given network except for network address and broadcast address
    online_hosts = []
    for host in hosts:
        if str(host) == network.network_address or str(host) == network.broadcast_address:
            continue
        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
        if response is None:
            print(str(host), "is down or unresponsive")
        elif response.type == 3 and response.code in [1, 2, 3, 9, 10, 13]:
            print(str(host), "is actively blocking ICMP traffic")
        else:
            print(str(host), "is responding")
            online_hosts.append(str(host))

    # Count how many hosts are online and inform the user
    print("Total online hosts:", len(online_hosts))
    
else:
    print("Invalid choice. Please try again.")

    # End Code