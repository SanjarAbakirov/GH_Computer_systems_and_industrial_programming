import socket

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP connection
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP connection
server.bind(('0.0.0.0', 9999))  # automatically

# server.listen(5)  # how many connection are alllowed

while True:
    # client, addr = server.accept()
    # print(client.recv(1024).decode())
    # client.send("Hello from server".encode())
    data, addr = server.recvfrom(1024)
