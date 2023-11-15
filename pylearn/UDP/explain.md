# explain
```python
          //套接字   //接受数据缓冲区 //接受数据长度 //标志  
          ssize recvfrom(int sockfd, void *buf, size_t len, int flag, 
//数据发送者地址，函数调用后垓地址结构被回收 //地址长度指针
struct sockaddr *addr, socklen_t *addrlen)

ssize recv(int sockfd,void *buf, size_t len,int flag)
```
recvfrom可以获得发送者的地址，通常用于无连接套接字。否则recvfrom等同于recv

1. recvfrom 可同时应用于面向连接和面向无连接的套接字，而recv一般面对连接的套接字，几乎等同于recvfrom,因此recv应用的场景recvfrom也可应用，将recvfrom第五个参数设置为NULL
