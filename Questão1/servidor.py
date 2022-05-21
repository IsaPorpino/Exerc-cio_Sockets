
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

dados =	{
    "Nome": "Isabela",
    "CPF": "000.000.000-00",
    "RG": "3837952",
    "Data de nascimento": "24/06/2000",
    "Matrícula": "18070041",
    "Curso": "Direito"

}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                dec = str(data.decode())[:-1]
                palavra = str.encode(dados[dec])
                print(palavra)
            #conn.sendall()
            conn.sendall(palavra)

