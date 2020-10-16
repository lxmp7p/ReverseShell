import socket
import sys
import os
import random

def send_file(file_path):
	try:
		while True:	
			sock = socket.socket()
			sock.connect(('localhost', 1010))
			file = open(file_path, "rb")
			file_size = sys.getsizeof(file)
			i = 0
			sock.send(b'BEGIN')
			print(file_size)
			while True:
				print('send')
				data = file.read(1024) # считать 1024 байт
				sock.send(data)
				if not data:
					print('Breaking from sending data')
					sock.send(b'ENDED')
					print('loool')
					break
			file.close()
	except Exception as e:
		print('error')
		file.close()	


#SERVER
def download_file():
	sock = socket.socket()
	sock.bind(('', 1010))
	sock.listen(1)
	file = open(str(random.randint(1,1000))+".txt", 'wb')
	try:
		while True:
			i = 0
			conn, addr = sock.accept()
			data = conn.recv(32)
			if data == b'BEGIN':
				print('begin')
				while True:
					data = conn.recv(1024)
					if (data == b'ENDED'):
						conn.close()
						file.close()
						break
					file.write(data)
			if (data == b'ENDED'):
				print('Breaking from file write')
				file.close()
				conn.close()
				break
	except Exception as e:
		print('error')
		file.close()
		conn.close()
'''
			if (message == 'exit'):
				conn.close()
				break
			if (message == 'shutdown'):
				sys.exit()
			if not data:
				break

			conn.send(data.upper())
'''		

'''
mode = input("Запустить как:\n1)Клиент\n2)Сервер:\nВаш выбор: ")
if mode=='1':
	start_client()
if mode=='2':
	start_server()
'''