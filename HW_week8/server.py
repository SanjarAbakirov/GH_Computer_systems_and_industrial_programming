import socket
import threading  # multiple way to create multipule threads in one pipe line program

HEADER = 64  # 64 TELLS message that is going to come next
PORT = 5050
# means get the ip adress automatically of this computer
SERVER = socket.gethostbyname(socket.gethostname())

# print(socket.gethostname())  # name represent computer as adress
ADDR = (SERVER, PORT)
# what type of ip adress we are looking for - specific connetions
# default option for streaming data
FORMAT = 'UTF-8'
DISCONECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET - what type of IP adress we are looking for
# SOCK_STREAM - it is a method
server.bind(ADDR)  # bound socke to this adress


def handle_client(conn, addr):
    # hadle coomunication between client and server
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        connected = True
        while connected:
            # decode this msg from its bite format into string using UTF-8
            msg_length = conn.recv(HEADER).decode(FORMAT)
            # how many bites we are going to receive
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONECT_MESSAGE:
                    connected = False

            print(f"[{addr}] {msg}")  # handling the disconnection clearly

        conn.close()  # closed disconnection


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()  # waits new connection to the server
        # conn - object waits new connection fro the server
        # allow us to send information back
        # addr - is information of connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# stok_steam means we are using TCP - transmission contro protocol
start()
