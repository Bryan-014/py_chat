import socket

def start_server(host: str, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    print(f"Server started at {host}:{port}\nListening now...")

    clients = set()

    while True:
        data, addr = server.recvfrom(1024)
        print(f"[{addr}]: {data.decode()}")

        if data.decode() == 'Mensagem de Conexão'  and addr not in clients:
            clients.add(addr)
        else:
            for client in clients:
                if client != addr:
                    server.sendto(f"[{addr}] {data.decode()}".encode(), client)

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 8000
    start_server(HOST, PORT)
