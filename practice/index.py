# socket practice
import socket
# host = socket.gethostbyname(socket.gethostname()) #dynamicly - if using virtual box - will be not good
HOST = '192.168.31.127'
# HOST = '127.0.0.1'  # for local host
# HOST = 'Localhost'  # for local host
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
