# tipycal Transmission Control Protocol
import socket
import threading
from datetime import datetime

HEADER = 64
PORT = 5050
# means get the ip adress automatically of this computer
SERVER = socket.gethostbyname(socket.gethostname())  # TCP/IP
ADDR = (SERVER, PORT)
# what type of ip adress we are looking for - specific connetions
FORMAT = 'utf-8'
DISCONECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
server.bind(ADDR)  # bound socket to this adress (SERVER, PORT)


def create_http_responce(status_code, body, content_type="text/plain"):
    # created HTTP- response bar with status
    status_codes = {
        200: "200 Ok",
        201: "201 Created",
        400: "400 Bad request",
        404: "404 Not found",
        500: "500 Initial Server Error"
    }
    status_text = status_codes.get(status_code, "500 Internal Server Error")

    responce = f"HTTP/1.1 {status_text}\r\n"
    responce += f"Content-Type: {content_type}r\n"
    responce += f"Cknnect-Length: {len(body)}\r\n"
    responce += "Connection: close\r\n"
    responce += "\r\n"  # empty str - end of headers
    responce += body

    return responce


def handle_http_request(request):
    lines = request.split('r/n')
    request_line = lines[0]
    method, path, version = request_line.split('')
    print(f"[HTTP] {method} {path}")
    # processing different threads
    if path == "/":
        return create_http_responce(200, "Welcome to Sam's Server")
    elif path == "/status":
        return create_http_responce(200, "Server is running")
    elif path == "api/data":
        return create_http_responce(200, '{"data": "some json here"}')
    else:
        return create_http_responce(404, "Page not found")


def handle_client(conn, addr):  # HTTP
    print(f"[Warning! NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:  # the code will be occured if we receive message from client
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)

# our http request processing
                if msg.startswith("GET") or msg.startswith("POST"):
                    http_response = handle_http_request(msg)
                    conn.send(http_response.encode(FORMAT))
                elif msg == DISCONECT_MESSAGE:
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
