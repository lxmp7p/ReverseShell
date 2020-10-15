import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_server():
    s.bind(('0.0.0.0', 8888))
    s.listen(5)
    client, addr = s.accept()
    while True:
        command = str(input('Send command: '))
        client.send(command.encode())
        if command.lower() == 'exit':
            break
        result_output = client.recv(1024).decode()
        print(result_output)
    client.close()
    s.close()

start_server()