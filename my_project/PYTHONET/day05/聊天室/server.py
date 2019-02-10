#coding=utf-8
'''
Chartroom
socket and fork
'''

from socket import *
import os,sys

def do_login(s, user, name, addr):
    if (name in user) or name == '管理员':
        s.sendto("该用户已存在".encode(), addr)
        return
    s.sendto(b'OK', addr)
    #先通知其他人
    msg = "\n欢迎 %s 进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(), user[i])
    #将用户插入
    user[name] = addr

def do_chat(s, user, name, msg):
    msg = "\n%s 说: %s"%(name, msg)
    #循环发送给所有人,除了自己
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])

def do_quit(s, user, name):
    msg = "\n%s 退出了聊天室"%name
    for i in user:
        if i == name:
            s.sendto(b'EXIT', user[i])
        else:
            s.sendto(msg.encode(), user[i])
    #删除该用户
    del user[name]


def do_request(s):
    #存储结构:{'zhangsan':('127.0.0.1', 9999)}
    user = {}
    while True:
        msg, addr = s.recvfrom(1024)
        #按空格分隔字符串并保存在列表里
        msgList = msg.decode().split(' ')
        #区分请求类别
        if msgList[0] == 'L':
            do_login(s, user, msgList[1], addr)
        elif msgList[0] == "C":
            #将列表里分隔的元素重新合成字符串
            msg = ' '.join(msgList[2:])
            do_chat(s, user, msgList[1], msg)
        elif msgList[0] == 'Q':
            do_quit(s, user, msgList[1])
            
    # print(data.decode())

#创建网络连接
def main():
    ADDR = ('0.0.0.0', 8888)
    #创建套接字
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    #创建多进程, 一个处理客户端请求,另一个发送管理员消息
    pid = os.fork()
    if pid < 0:
        print("Create process failed")
        return
    #子进程发送管理员消息
    elif pid == 0:
        while True:                                                   
            msg = input("管理员消息:")
            msg = "C 管理员 " + msg
            s.sendto(msg.encode(), ADDR)
    #父进程处理客户端请求
    else:
        do_request(s)

main()
