import socket

# Configuración del cliente
host = '127.0.0.1'  # La dirección IP del servidor
port = 12345       # El puerto en el que el servidor está escuchando

# Crear un objeto de socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((host, port))

while True:
    message = input("Ingrese un mensaje: ")
    client_socket.send(message.encode('utf-8'))
    if message.lower() == 'adios':
        break
    response = client_socket.recv(1024).decode('utf-8')
    print("Respuesta del servidor:", response)

# Cerrar el socket del cliente
client_socket.close()
