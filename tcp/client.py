import socket

def start_client(address: str, port: int):
    client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    message = input('Digite uma menssagem: ').encode()

    client_server.connect((address,port))
    client_server.sendall(message)

if __name__=="__main__":
    DESTINATION = 'localhost'
    PORT = 6000
    start_client(DESTINATION,PORT)