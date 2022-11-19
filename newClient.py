#!/usr/bin/env python3

import socket

HOST = '192.168.1.8'
PORT = 3074

print("Please don't spam make use for the right Purpose :)");
print("Your messages are being monitored");
name = input("Your Sweet Name Please: ");

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((HOST, PORT))
print(s.recv(2048).decode())
while(True):
	msg = input("Message: ")
	if(msg == "quit"):
		break
	msg = name + ": " + msg
	s.sendall(msg.encode())
s.close()
	

