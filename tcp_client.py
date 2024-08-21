import socket

IP = '127.0.0.1'  # IP do servidor (use 127.0.0.1 para localhost)
PORT = 9998       # Porta do servidor

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))

    # Enviar uma mensagem para o servidor
    client.send(b'Hello, Server!')

    # Receber uma resposta do servidor
    response = client.recv(4096)
    print(f'[*] Received: {response.decode("utf-8")}')

    client.close()

if __name__ == '__main__':
    main()
