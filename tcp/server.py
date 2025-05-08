import socket

def start_server(address: str, port: int):
   server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   server_socket.bind((address,port))
   server_socket.listen(1)

   print(f'Server rodando.. {address}  {port}')

   while True:
      client_socket,client_address= server_socket.accept()
      data = client_socket.recv(1024)
      print(f'{client_address}-Messagem: {data.decode()}')
      client_socket.close()


if __name__=="__main__":
   try:
      HOST = 'localhost'
      PORT = 6000

      start_server(HOST, PORT)
   except Exception as e:
      print(e)