import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP connection
# client.connect(('127.0.0.1', 9999))

# client.send(f"Hello from client".encode())
client.sendto('Hello from client'.encode(), ("127.0.0.1", 9999))
# print(client.recv(1024).decode())
data, addr = client.
