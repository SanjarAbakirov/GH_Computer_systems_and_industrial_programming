import socket
import threading  # multiple way to create multipule threads in one pipe line program

HEADER = 64  # 64 TELLS message that is going to come next
PORT = 5050
# SERVER = "192.168.31.127"
SERVER = socket.gethostbyname(socket.gethostname())
# means get the ip adress of this computer

# print(socket.gethostname())  # name represent computer as adress
ADDR = (SERVER, PORT)
# what type of ip adress we are looking for - specific connetions
# default option for streaming data
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    # hadle coomunication between client and server
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        connected = True
        while connected:
            # decode this msg from its bite format into string using UTF-8
            msg_lenght = conn.recv(HEADER).decode(FORMAT)
            # how many bites we are going to receive
            if msg_lenght
            msg_length = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
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
