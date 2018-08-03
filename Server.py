# -*- coding:utf-8 -*-
import asyncore
from ChatSession import ChatSession
from Hall import Hall
class ChatHandler(asyncore.dispatcher_with_send):
    def __init__(self,socket):
        super(ChatHandler,self).__init__(socket)
        self.size_buff = 1024

    # 可读时调用
    def handle_read(self):
        data = self.recv(self.size_buff)
        if not data:
            self.close()
        else:
            pass

    # 连接关闭时调用
    def handle_close(self):
        print("关闭")
        self.close()


class ChatServer(asyncore.dispatcher):
    def __init__(self,host,port,listen_number):
        super(ChatServer,self).__init__()
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host,port))
        self.listen(listen_number)
        self.chat_session = ChatSession()
        self.hall = Hall()

    def handle_accepted(self, sock, addr):
        print("{addr}连接进来".format(addr = addr))
        handler = ChatHandler(sock)
        self.hall.Login(sock)






if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8087
    listen_number = 10
    server = ChatServer(host,port,listen_number)
    asyncore.loop()


