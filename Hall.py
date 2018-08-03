# -*- coding:utf-8 -*-
class Hall(object):
    '''
        大厅类，用于处理名称输入，退出服务器，加入聊天室/创建聊天室
    '''

    def __init__(self):
        self.size_buff = 1024

    def Login(self, socket):
        socket.sendall("请输入你的名字".encode("utf-8"))
