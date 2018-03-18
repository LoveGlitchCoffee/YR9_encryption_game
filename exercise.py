################################
# Imports, you can import more if you like
from utils import *
init() # Do not change this
###############################


###########################################
# Your hacking details
# You can change nearly anything you like here
###########################################

YOUR_IP_ADDRESS = "192.3.24.1"
YOUR_PORT = "20"
YOUR_PROTOCOL = "UDP"
DESTINAION_IP_ADDRESS = "184.5.2.3"
DESTINATION_PORT = "38"
# Firewall Structure:
# Permission Type | Protocol | Source IP | Source Port | Destination IP | Destination Port
THEIR_FIREWALL = [
   ["ALLOW", "UDP", "183.2.4.1", "80", "194.3.2.4", "80"],
   ["ALLOW", "TCP", "294.2.5.2", "90", "194.3.2.4", "80"]
]

def your_encryption_cracker(phrase):
    # phrase is an array of characters
    print("You have not implemented your cracker")
    # please write your brute force password cracker here

#############################################


################################
# The exercises, Do not change
###############################
sequence1(YOUR_PROTOCOL, YOUR_IP_ADDRESS, YOUR_PORT,  DESTINAION_IP_ADDRESS, DESTINATION_PORT, THEIR_FIREWALL)
sequence2(your_encryption_cracker)
sequence3()
###############################