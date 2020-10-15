import socket
import sys
import os

def start_client():
	while True:	
		sock = socket.socket()
		sock.connect(('192.168.0.104', 1010))
		message = input("Input: ")
		if (message == 'exit'):
			sock.close()
			break
		if (message == 'shutdown'):
			sock.send(message.encode())
			sock.close()
			break
		file = open('1.jpg', 'rb')
		for i in file:
			sock.send(i)
		data = sock.recv(1024)
		file.close()
		#print(data)



#SERVER
def start_server():
	sock = socket.socket()
	sock.bind(('0.0.0.0', 1010))
	sock.listen(1)
	while True:
		conn, addr = sock.accept()
		while True:
			data = conn.recv(1024)
			message = data
			file = open('a.jpg', 'wb')
			file.write(message)
			file.close()
			if (message == 'exit'):
				conn.close()
				break
			if (message == 'shutdown'):
				sys.exit()
			if not data:
				break
			#conn.send(data.upper())


mode = input("Запустить как:\n1)Клиент\n2)Сервер:\nВаш выбор: ")
if mode=='1':
	start_client()
if mode=='2':
	start_server()
