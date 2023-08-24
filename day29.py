#网络编程
#Ip:把数据通过Ip包的形式从一台计算机发送到另一台计算机
#Tcp:负责在两台计算机之间建立可靠连接，保证数据包按顺序到达

#Tcp编程：建立可靠连接，通信双方都可以以流的形式发送数据
# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET指定使用IPv4协议，SOCK_STREAM指定使用面向流的TCP协议
# 建立连接:
s.connect(('49.232.147.237', 80))#参数是地址和端口号
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: 49.232.147.237\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接:
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)

#UDP编程：不需要网络连接，需要知道对方的IP地址和端口号，就可以直接发数据包。
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # 绑定端口:
# s.bind(('127.0.0.1', 9999))
# print('Bind UDP on 9999...')
# while True:
#     # 接收数据:
#     data, addr = s.recvfrom(1024)
#     print('Received from %s:%s.' % addr)
#     s.sendto(b'Hello, %s!' % data, addr)