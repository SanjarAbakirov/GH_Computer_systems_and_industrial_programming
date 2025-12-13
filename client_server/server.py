import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP connection
server.bind(('0.0.0.0', 9999))

server.listen(5)

while True:
    client, add = server
