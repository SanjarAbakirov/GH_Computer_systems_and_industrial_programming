import socket

HEADER = 64  # 64 TELLS message that is going to come next
PORT = 5050
FORMAT = 'utf-8'
DISCONECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.31.127"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
