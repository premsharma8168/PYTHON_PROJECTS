import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = ('localhost', 1234)
# address= (socket.gethostname(), 1234)
s.connect(address)
while 1:
    data = input('client: ').encode()
    s.send(data)
    res = s.recv(1024)
    print('Server:', res.decode())
s.close()
