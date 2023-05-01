#!/usr/bin/env python3

# Script: Ops 401 Class 11 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 1MAY2023
# Purpose: TCP Port Range Scanner
# Resources Alex's demo, Chatgpt, google
    #REQUIREMENTS
#Utilize the scapy library
#Define host IP
#Define port range or specific set of ports to scan
#Test each port in the specified range using a for loop
#If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
#If flag 0x14 received, notify user the port is closed.
#If no flag is received, notify the user the port is filtered and silently dropped.
    #DEMO
#!/usr/bin/python3

# Utilize the scapy library
#from scapy.all import ICMP, IP, sr1, TCP

# Define host IP
#host = "scanme.nmap.org"
# Define port range or specific set of ports to scan
#port_range = [22, 23, 80, 443, 3389]
# Test each port in the specified range using a for loop
#for dst_port in port_range:
#  src_port = 1025
#  response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port,flags="S"), timeout=1, verbose=0)
  # print(response.summary) # a little info
  # print(response.show()) # A LOT OF INFO
  # If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
#  if(response.haslayer(TCP)):
#    if(response.getlayer(TCP).flags == 0x12):
      # PORT IS OPEN!!
  # If flag 0x14 received, notify user the port is closed.
  # If no flag is received, notify the user the port is filtered and silently dropped.1

    # Start Code
# Utilize the scapy library
from scapy.all import ICMP, IP, sr1, TCP

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

    # End Code