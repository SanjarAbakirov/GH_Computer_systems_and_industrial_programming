import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP connection
server.bind(('0.0.0.0', 9999))  # automatically

server.listen(5)  # how many connection are alllowed

while True:
client, addr = server
