import socket
import threading

def receive_messages(sock):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print(f"\n[{addr}]: {data.decode()}")
        except:
            continue

def send_message(host: str, port: int):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind(('', 0))
    client.settimeout(1)

    listener = threading.Thread(target=receive_messages, args=(client,), daemon=True)
    listener.start()

    print("Conectado ao chat. Pressione Ctrl+C para sair.")
    
    try:
        while True:
            msg = input()
            client.sendto(msg.encode(), (host, port))
    except KeyboardInterrupt:
        print("\nSaindo do chat.")

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 8000
    send_message(HOST, PORT)
