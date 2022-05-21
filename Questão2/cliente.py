import sys
import socket

#pra testar ficava mais fácil ter os endereços fixos
#HOST = '127.0.0.1'
#PORT = 65432

HOST = str(sys.stdin.readline())[:-1]
PORT = int(str(sys.stdin.readline())[:-1])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("insira o comando que deseja executar:")
    pesquisa = str.encode(sys.stdin.readline())
    s.sendall(pesquisa)
    data = s.recv(1024).decode()

print(data)