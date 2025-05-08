import socket

def send_message(host: str, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.settimeout(1)
    
    
    while True:
        message = input('type your message: ')
        server.sendto(message.encode(), (host, port))
        
        data, addr = server.recvfrom(1024)
        print(f'[Message]: {data.decode()}')
        

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 8000
    
    send_message(HOST, PORT)