import socket
import threading  # multiple way to create multipule threads in one pipe line program

PORT = 5050
# SERVER = "192.168.31.127"
SERVER = socket.gethostbyname(socket.gethostname())
# means get the ip adress of this computer
print(SERVER)
print(socket.gethostname())  # name represent computer
# so let's put address to this server
ADDR = (SERVER, PORT)

# what type of ip adress we are looking for specific connetions
# default option for streaming data
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    pass


def start():
    pass


print("[STARTING] server is starting...")
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# stok_steam means we are using TCP - transmission contro protocol
