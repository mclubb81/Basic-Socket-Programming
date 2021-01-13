# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:39:37 2020
Server Program
@author: clubb
"""

import socket
from des import DesKey
import _thread 
import threading 

# Key for encryption/decryption
key = DesKey(b"153764816573465982461538")

# Multithreading
print_lock = threading.Lock()
 
def threaded(conn): 
    while True:
        # Recieving data from client
        data = conn.recv(1024)
        if not data: 
            # lock released on exit 
            print_lock.release() 
            break
        print("Message received!")
                
        # Decrypting message from client
        data = key.decrypt(data, padding = True)
                
        # Converting client message to UPPER CASE
        data = data.upper()
        print("Responding with message:", data)
                
        # Encrypting response
        data = key.encrypt(data, padding = True)
                
        # Sending data back to client
        conn.sendall(data)
        print("")


HOST = ''
PORT = 50007              
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    
    # Listening for client connections
    s.listen(5)
    print("Listening...")
       
    while True:
        # establishing connection with client
        conn, addr = s.accept()
        print('Connected to :', addr[0], ':', addr[1])
        
        # Start a new thread
        _thread.start_new_thread(threaded, (conn, ))
        
        # lock acquired 
        print_lock.acquire() 
         
                
            
        

