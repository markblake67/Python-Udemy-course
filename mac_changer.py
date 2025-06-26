#!/usr/bin/env python

import subprocess

interface = "eth0"
new_mac = "12:11:22:33:44:00" #New MAC has to start with even octet

print(f"[+] Changing MAC address for {interface} to {new_mac}") #Test print

#All these commands can be run command?
subprocess.call(f"ifconfig {interface} down", shell=True)  #sets eth0 the ethernet interface to down, need to do before changing MAC. Can also be run
subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True) #sets the MAC address (found in 'ether' section to this number. Tells the shell to run as True
subprocess.call(f"ifconfig {interface} up", shell=True) #puts eth0 back up.
subprocess.call(f"ifconfig", shell=True) #runs ifconfig again to show changed MAC.
