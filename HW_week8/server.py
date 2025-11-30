# tipycal Transmission Control Protocol
import socket
import threading

HEADER = 64
PORT = 5050
# means get the ip adress automatically of this computer
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
# what type of ip adress we are looking for - specific connetions
FORMAT = 'utf-8'
DISCONECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)  # bound socket to this adress (SERVER, PORT)


def handle_client(conn, addr):
    print(f"[Warning! NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:  # the code will be occured if we receive message from client
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)

                if msg == DISCONECT_MESSAGE:
                    connected = False
                    print(f"[{addr}] disconnected")
                else:
                    print(f"[{addr}] {msg}")
        except:
            print(f"[ERROR] with {addr}: {e}sss")
            break

    conn.close()  # closed disconnection


def start():
    server.listen()
    print(f"[READY TO RECEIVE DATA] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()  # waits new connection to the server
        # conn - object waits new connection fro the server
        # allow us to send information back
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    # conn.settimeout(5)
print("[STARTING] server is starting...")
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# stok_steam means we are using TCP - transmission contro protocol
start()
