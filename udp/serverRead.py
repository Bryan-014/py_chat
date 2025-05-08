import socket

def send_message(host: str, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server.bind((host, port))
    print(f"Server started at {host}:{port}\n Listening now...")
    
    while True:                
        data, addr = server.recvfrom(1024)
        print(f'[{addr}]: {data.decode()}')            

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 8800
    
    send_message(HOST, PORT)
