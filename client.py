import socket


while True:
    sock = socket.socket()
    sock.connect(('localhost', 9090))
    sock.send(input().encode())

    data = sock.recv(1024)
    sock.close()

    print (data.decode())