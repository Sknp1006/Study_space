from socket import *

#执行函数中处理请求
def handle(connfd):
    print("Connect from", connfd.getpeername())
    request = connfd.recv(4096) #获取http请求
    #将请求按行切割
    request_lines = request.splitlines()
    #打印http协议的每一行
    for line in request_lines:
        print(line)
    
    #给浏览器客户端返回响应
    try:
        f = open('index.html')  #默认字符串打开
    except IOError:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += '\r\n'
        response += '===Sorry not found the page==='
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += '\r\n'
        while True:
            data = f.read(4096)
            if not data:
                break
            response += data
    finally:
        #将结果发送给客户端
        connfd.send(response.encode())
        f.close()

#在主函数里创建套接字
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(('0.0.0.0', 8000))

    sockfd.listen(5)
    print("Listen to the port 8000......")

    while True:
        connfd, addr = sockfd.accept()
        #处理客户端请求
        handle(connfd)
        connfd.close()

main()
