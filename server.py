#Codenation - Aula de Socket
import socket

#Mostrando a comunicacao entre o server, neste caso meu próprio PC, com o cliente
#(cliente criado com nome "cliente.py")

HOST = '127.0.0.1'
PORT = 65432

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        print(f'Esperando conexão em {HOST}:{PORT}')
        conn, addr = s.accept()
        with conn:
            print('Conectado por',addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(b'Server' + data)

