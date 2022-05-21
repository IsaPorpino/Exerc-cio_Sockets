import socket
import sys
import subprocess
from _thread import *

s = socket.socket()

#[:-1] tirar o \n do final da string
host = str(sys.stdin.readline())[:-1]
port = int(str(sys.stdin.readline())[:-1])

#pra testar ficava mais fácil ter os endereços fixos
#host = '127.0.0.1'
#port = 65432

ThreadCount = 0

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
s.listen(5)


def multi_threaded_client(conn):

    while True:
        cmd = conn.recv(1024)

        #[:-1] tirar o \n do final da string
        dec = cmd.decode()[ :-1]

        if not cmd:
            break

        # executa o comando e imprime resultado
        status_output = subprocess.getstatusoutput(dec)
        print(status_output)

        conn.sendall(cmd)
    conn.close()


while True:
    Client, address = s.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client,))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))

s.close()