import time
import random
import sys

password = ""
x = ""
random.seed(8)
list_of_chars = "0123456789ABCDEF"
phrase_array = ['u', ' ', 'j', 'x', 'o', 'h', 'p', ' ', 'q', 'e', 'b', ' ', 'p', 'm', 'l', 'q', ',', ' ', 'm', 'x', 'p', 'p', 't', 'l', 'o', 'a', ' ', 'f', 'p', ' ', '_','_','_','q','b','p','q','f','k','d']

def jumpStartSecurity():
   i = 20
   p = ""
   for j in range(0, i):
      p += str(i)
   
def lockdown():
   password_arr = ['pen', 'book', 'testing', 'code']
   return password_arr


def bypass(your_protocol, your_ip_address, your_port, destinaion_ip_address, destination_port, their_firewall):
   bypassed = False
   try:
      for r in their_firewall:
         if r[0] == "ALLOW" and (r[1] == your_protocol or r[1] == "ANY") and (r[2] == your_ip_address or r[2] == "ANY") and (r[3] == your_port or r[3] == "ANY") and (r[4] == destinaion_ip_address or r[4] == "ANY") and (r[5] == destination_port or r[5] == "ANY"):
            bypassed = True
            break
   except:
      print("You changed something you should have about firewall, please check")
   return bypassed


def init():
   global password, x
   jumpStartSecurity()
   password += "1"
   for letter in range(0, 1):
       password += list_of_chars[random.randint(0, 16)]
   p = lockdown()
   x = p[0] + p[2]   

def sequence1(YOUR_PROTOCOL, YOUR_IP_ADDRESS, YOUR_PORT,  DESTINAION_IP_ADDRESS, DESTINATION_PORT, THEIR_FIREWALL):
   print("Initiate hacking sequence")

   # Exercise 1
   print ("Need to bypass Firewall first, change your details or their firewall rules")
   # Change either
   pressed = input("Press 'Enter' to continue")

   if bypass(YOUR_PROTOCOL, YOUR_IP_ADDRESS, YOUR_PORT,  DESTINAION_IP_ADDRESS, DESTINATION_PORT, THEIR_FIREWALL):
      print("Firewall bypassed, password hint: U jxohp qeb pmlq, mxpptloa fp ___qbpqfkd")
   else:
      print("Firewall reject, please try again")
      sys.exit()

def sequence2(cracker):   
   print("Your cracker will now run")
   cracker(phrase_array)
   print("Can you see the deciphered hint?")

def sequence3():
   correct = False
   while not correct:
      p = input("Please type in the password: ")
      if p == x:
         print("You are in the system, well done, please report vulnerabilities")
      else:
         print("incorrect password, Rejected")