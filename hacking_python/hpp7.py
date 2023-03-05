import socket

# Crear un objeto socket para el servidor
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Especificar el número de puerto en el que se va a escuchar
puerto = 8080

# Enlazar el servidor con el puerto especificado
servidor_socket.bind(('192.168.28.144', puerto))

# Empezar a escuchar conexiones entrantes
servidor_socket.listen()

print('El servidor está escuchando en el puerto', puerto)

while True:
    # Esperar una conexión entrante
    conexion, direccion = servidor_socket.accept()
    print('Se ha establecido una conexión desde', direccion)

    # Recibir datos de la conexión entrante
    while True:
        datos = conexion.recv(1024)
        if not datos:
            break

        # Procesar los datos recibidos
        mensaje = datos.decode('utf-8')
        print('Se ha recibido el siguiente mensaje:', mensaje)

    # Cerrar la conexión entrante
    conexion.close()