import socket

# Configuración del servidor
host = '127.0.0.1'  # La dirección IP del servidor
port = 12345       # El puerto en el que escuchará el servidor

# Crear un objeto de socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket al host y al puerto
server_socket.bind((host, port))

# Escuchar conexiones entrantes
server_socket.listen()

print("Esperando una conexión entrante...")

# Aceptar una conexión entrante
client_socket, client_address = server_socket.accept()

print(f"Conexión establecida con {client_address}")

# Recibir y enviar datos
while True:
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    print(f"Mensaje recibido: {data}")
    response = f"Recibido: {data}"
    client_socket.send(response.encode('utf-8'))

# Cerrar sockets
client_socket.close()
server_socket.close()
