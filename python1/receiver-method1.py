# DNS Exfiltration 1 Receiver
# 
# For educational purposes only!
#
# This script is the server-side of the exfiltration script 'sender-method1.py', receives and prints DNS A query to obtain message

from scapy import all
from scapy.all import *


net_interface = "lo" # Set the listening interface
sender = "1.2.3.4" # IP of the exfiltrator (sender)

packet_filter = " and ".join([
    "udp dst port 53",          # Filter UDP port 53
    "udp[10] & 0x80 = 0",       # DNS queries only
    "src host " + sender    # IP source <ip>
    ])

sniff(filter=packet_filter, iface=net_interface, prn=lambda x:x.summary()) #Sniff packets based on filter, print results
