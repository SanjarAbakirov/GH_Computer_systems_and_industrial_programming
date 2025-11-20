import socket

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISCONECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.26"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect()
