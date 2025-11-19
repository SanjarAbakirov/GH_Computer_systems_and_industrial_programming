import socket
import threading  # multiple way to create multipule threads in one pipe line program

PORT = 5050
# SERVER = "192.168.31.127"
SERVER = socket.gethostbyname(socket.gethostname())
# means get the ip adress of this computer
# print(SERVER)
# print(socket.gethostname()) # name reoresent computer

# so let's put address to this server
ADDR = (SERVER, PORT)

# what type of ip adress we are looking for specific connetions
# default option for streaming data
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# stok_steam means we are using TCP - transmission contro protocol
