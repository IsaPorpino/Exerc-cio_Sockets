import sys
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Informação para pesquisa: (Nome, CPF, RG, Data de nascimento, Matrícula, Curso)")
    pesquisa = str.encode(sys.stdin.readline())
    s.sendall(pesquisa)
    data = s.recv(1024).decode()

print(data)