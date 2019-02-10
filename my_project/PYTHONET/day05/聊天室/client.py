#coding=utf-8
from socket import *
import os,sys

def recv_msg(s):
    while True:
        data, addr = s.recvfrom(1024)
        #服务器发来EXIT表示要退出
        if data.decode() == 'EXIT':
            sys.exit(0)
        print(data.decode() + '\n消息:', end="")

def send_msg(s, name, addr):
    while True:
        text = input("消息:")
        if text == '##':
            msg = 'Q ' + name
            s.sendto(msg.encode(), addr)
            sys.exit("退出聊天室")
        msg = "C %s %s"%(name, text)
        s.sendto(msg.encode(), addr)
    
#创建套接字
def main():
    #从命令行输入IP
    if len(sys.argv) < 3:
        print("argv is error!!")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)

    # 创建套接字
    s = socket(AF_INET, SOCK_DGRAM)
    # s.sendto(b'zhangsan', ADDR)

    #先登录,再聊天
    while True:
        name = input("请输入姓名:")
        #L 开头,表示登录消息
        msg = 'L ' + name
        s.sendto(msg.encode(), ADDR)
        #等待回应
        data, addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break
        else:
            print(data.decode())
    
    #创建父子进程
    pid = os.fork()
    if pid < 0:
        sys.exit("创建进程失败")
    elif pid == 0:
        #子进程发送息消息
        send_msg(s, name, addr)
    else:
        #父进程接收消息
        recv_msg(s)  #接收消息
        

main()
