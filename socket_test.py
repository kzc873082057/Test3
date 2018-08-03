# -*- coding:utf-8 -*-
import socket
class Client(object):
    def __init__(self,address):
        self.address = address
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_conn = False
        self.size_buff = 2048
        self.conn()

    def conn(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.address)
        self.is_conn = True

client = Client(("127.0.0.1",8087))
data = client.client_socket.recv(1024).decode("utf-8")
print(data)
client.client_socket.sendall("1231321".encode("utf-8"))
while True:
    pass
