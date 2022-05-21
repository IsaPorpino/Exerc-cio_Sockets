import socket

s = socket.socket()
s.connect(("www.example.com", 80))
s.send(b"GET / HTTP/1.1\r\nHost:www.example.com\r\n\r\n")
response = s.recv(1024)
s.close()
print(response.decode())
with open('colar.txt', 'w') as f:
    f.write(response.decode())