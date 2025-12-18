# socket practice
import socket
host = socket.gethostbyname(socket.gethostname())
HOST = '192.168.31.127'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
