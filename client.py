# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:43:47 2020
Client Program
@author: clubb
"""
import socket
from des import DesKey

# Key for encryption/decryption
key = DesKey(b"153764816573465982461538")

HOST = '127.0.0.1'    # The local host
PORT = 50007          # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    while True:
        # Asks client to enter message
        client_message = input("Enter your message:")
        
        # Converting client string to bytes 
        client_message = bytes(client_message, 'utf-8') 
        
        # Encrypting client message
        client_message = key.encrypt(client_message, padding = True)
        
        # Sending message to server
        s.sendall(client_message)
        
        # Data recieved from server
        print("Waiting for response...")
        data = s.recv(1024)
        print("Received response!")
        
        # Decrypting response from server
        data = key.decrypt(data, padding = True)
        print('Received From Server:', repr(data))
        print("")
        
        # ask the client if they want to continue 
        client_ans = input('Do you want to continue(y/n) :') 
        if client_ans == 'y': 
            continue
        else: 
            break
    # close the connection 
    s.close() 
