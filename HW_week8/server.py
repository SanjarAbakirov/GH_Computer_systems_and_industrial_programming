import socket
import threading  # multiple way to create multipule threads in one pipe line program

PORT = 5050
# SERVER = "192.168.31.127"
SERVER = socket.gethostbyname(socket.gethostname())


# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# stok_steam means we are using TCP - transmission contro protocol
