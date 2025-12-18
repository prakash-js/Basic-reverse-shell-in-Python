import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 1234))
server.listen(5)
print("Server is Listening ... .. .")

while True:
    cli_socket, cli_addr = server.accept()
    data = cli_socket.recv(1024)
    print(data.strip().decode())

    while True:

        while True:
            sender_data = input(">>>").strip()
            if sender_data.strip():
                break

        if sender_data.startswith("get "):
            cli_socket.send(sender_data.encode())
            filename = sender_data[4:].strip()
            fileS = cli_socket.recv(1024).decode()
            file_size = int(fileS.strip())
            received_size = 0
            with open(filename, 'wb') as file:
                while received_size < file_size:
                    recv_data = cli_socket.recv(1024)
                    file.write(recv_data)
                    received_size += len(recv_data)
                    if recv_data == file_size:
                        break

        elif sender_data.startswith("upload "):
            cli_socket.send(sender_data.encode())
            print(cli_socket.recv(1024).decode())

        else:
            cli_socket.send(sender_data.encode())
            cmd_data = cli_socket.recv(2048)
            print(cmd_data.decode())
