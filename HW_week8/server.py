import socket
import threading  # multiple way to create multipule threads in one pipe line program

PORT = 5050
# SERVER = "192.168.31.127"
SERVER = socket.gethostbyname(socket.gethostname())
# means get the ip adress of this computer
# print(SERVER)
# print(socket.gethostname()) # name reoresent computer

# what type of ip adress we are looking for specific connetions
socket = socket.socket(socket.AF_INET)

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# stok_steam means we are using TCP - transmission contro protocol
