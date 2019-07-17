import socket
 
s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))

while True:
    data = s.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
s.close()