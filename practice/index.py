# socket practice
import socket
# host = socket.gethostbyname(socket.gethostname()) #dynamicly - if using virtual box - will be not good
HOST = '192.168.31.127'
# HOST = '127.0.0.1'  # for local host
# HOST = 'Localhost'  # for local host
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# how many unexepted connection we will allowed to reject a new one
server.listen(5)

while True:
    communiction_socket, address = server.accept()  # communication method
    print(f"Connected to {address}")
    message = communiction_socket.recv(1024).decode(
        'utf-8')  # expecto receive message from the client
    print(f"Message from clent is: {message}")
    communiction_socket.send(f"Got your message! Thank you!".encode('utf-8'))
    communiction_socket.close()
    print(f"Connection with {address} ended!")
# create client now
