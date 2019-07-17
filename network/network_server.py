import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))


while True:
    try:
        print("Wait connection...")
        s.settimeout(1)
        s.listen(5)
        c, addr = s.accept()
        if c is not None:
            print('Peer Address : ', addr)
            c.send('Welcome!!!'.encode())
            c.close()
    except socket.timeout:
        pass