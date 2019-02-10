from socketserver import *

#创建服务器类
# class Server(ForkingMixIn, TCPServer):   #多进程并发
# class Server(ForkingTCPServer):            #多进程并发
# class Server(ThreadingMixIn, TCPServer):   #多线程并发
class Server(ThreadingTCPServer):          #多线程并发
    pass

#具体请求处理类
class Handler(StreamRequestHandler):
    #具体处理方法
    def handle(self):
        print("Connect from", self.client_address)
        while True:
            #request相当于accept返回的连接套接字
            data = self.request.recv(1024)  
            if not data:
                break
            print(data.decode())
            self.request.send(b'OK')

#创建服务器对象,绑定处理类
server_addr = ('0.0.0.0', 8888)
server = Server(server_addr, Handler)
server.serve_forever()  #启动服务