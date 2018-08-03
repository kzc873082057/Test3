# -*- coding:utf-8 -*-
class ChatSession(object):
    '''
        用户会话创建实例，保持用户昵称，处理服务器与客户端的消息传递
    '''
    def __init__(self):
        self.user_list = {}

    # 添加用户
    def AddUser(self, username, socket):
        socket_info = {}
        socket_info.setdefault("username",username)
        self.user_list.setdefault(socket, socket_info)
        return

    # 删除用户
    def DeleteUser(self, socket):
        if self.user_list.get(socket):
            return self.user_list.pop(socket)
        else:
            return False

    # 查询用户是否存在
    def HasUser(self,socket):
        if self.user_list.get(socket):
            return True
        else:
            return False
