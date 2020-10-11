import socket
import sys
import os

def start_client():
	while True:	
		sock = socket.socket()
		sock.connect(('localhost', 1010))
		message = input("Input: ")
		if (message == 'exit'):
			sock.close()
			break
		if (message == 'shutdown'):
			sock.send(message.encode())
			sock.close()
			break
		sock.send(message.encode())
		data = sock.recv(1024)
		print(data)



#SERVER
def start_server():
	sock = socket.socket()
	sock.bind(('', 1010))
	sock.listen(1)
	while True:
		conn, addr = sock.accept()
		while True:
			data = conn.recv(1024)
			message = data.decode()
			if (message == 'exit'):
				conn.close()
				break
			if (message == 'shutdown'):
				sys.exit()
			if not data:
				break
			conn.send(data.upper())


mode = input("Запустить как:\n1)Клиент\n2)Сервер:\nВаш выбор: ")
if mode=='1':
	start_client()
if mode=='2':
	start_server()
