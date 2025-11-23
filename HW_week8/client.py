import socket

HEADER = 64  # 64 TELLS message that is going to come next
PORT = 5050
FORMAT = 'utf-8'
DISCONECT_MESSAGE = "!DISCONNECT check out the network"
SERVER = "192.168.31.127"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAR)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send("Hello!")
