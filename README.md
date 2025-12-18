# Basic-reverse-shell-in-Python
A basic reverse shell script in Python that connects to a specified IP and port, allowing command execution on the client machine.

reverseshell.py runs on the target system and initiates a connection back to the attacker machine.
server.py runs on the attacker machine and is used to communicate with the reverse shell.
The reverse shell allows remote command execution and supports file retrieval from the client system without relying on external file transfer services.
After a successful connection is established, files can be retrieved using the following command:

`get <filename>`


For Educational Use Only: Created for learning and testing in controlled environments. Unauthorized or malicious use is illegal and unethical. Use responsibly.
