#!/usr/bin/env python3


import socket
from threading import Thread

hostname = '192.168.1.8'
port = 3074

def start_chat(conn, addr):
	t = ChatMsg(conn, addr)
	t.start()
	print("Connected with IP: {} and port: {}".format(addr[0], addr[1]))
	
 
class ChatMsg(Thread):
	def __init__(self, conn, addr):
		Thread.__init__(self)
		self.conn = conn
		self.addr = addr
		
	def run(self):
		self.conn.sendall(b"Send your message.\n")
		while(True):
			try:
				data = self.conn.recv(2048)
				if not data:
					self.conn.close()
					continue
				else:
					try:
						data = data.decode()
						print(data)
					except:
						pass
			except:
				pass
						

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((hostname, port))
s.listen()
while(True):
	conn, addr = s.accept()
	start_chat(conn, addr)
s.close()

