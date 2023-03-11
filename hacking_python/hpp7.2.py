from pathlib import Path
from argparse import ArgumentParser
import re
from colorama import Fore, Style

patrones = {
    "password" :r'password',
    "usuario" :r'usuario',
    "URL" :r'http://',
    "SSH" :r'ssh',
    "FTP" :r'ftp',
    "Login" :r'login',
    "IPv4" :r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
    "Email" :r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
}

def detectar_patrones(fichero: Path):
    """
    Función que detecta patrones en un fichero a través de expresiones regulares

    :param fichero: Fichero a analizar
    :type fichero: Path
    :return: Lista de tuplas con los patrones detectados
    :rtype: list
    """
    lineas = fichero.read_text(encoding="utf-8").splitlines()
    detecciones = []
    for linea in lineas:
        for key, patron in patrones.items():
            if re.search(patron, linea):
                
                grupo = re.search(patron, linea, re.IGNORECASE).group()
                idx = linea.index(grupo)
                linea_idx = lineas.index(linea)
                start = idx - 10
                end = idx + len(grupo) + 10
                if start < 0:
                    start = 0
                if end > len(linea):
                    end = len(linea)
                fragment = linea[start:end].strip()
                # Color the pattern in the fragment
                fragment = fragment.replace(grupo, Fore.LIGHTGREEN_EX + grupo + Style.RESET_ALL)
                detecciones.append((fichero.name, key, grupo, linea_idx, idx, fragment.strip()))
    return detecciones



def obtener_ficheros(input: Path, host: str = None):
    """
    Función que obtiene los ficheros de un directorio

    :param input: Directorio donde están los ficheros
    :type input: Path
    :param host: Host a filtrar, por defecto None
    :type host: str, optional
    :return: Lista de ficheros
    :rtype: list
    """
    paths = []
    for fichero in input.glob('*.txt'):
        if host:
            if host in fichero.name:
                paths.append(fichero)
        else:
            paths.append(fichero)
    return paths

def main():
    parser = ArgumentParser(description="Detector de patrones en ficheros keylogs")
    parser.add_argument('-i', '--input', help="Carpeta donde están los ficheros keylogs", default="files", type=str)
    parser.add_argument('-t', '--target', help="Host a filtrar", default=None, type=str)
    args = parser.parse_args()

    ruta = Path(__file__).parent / args.input
    if not ruta.exists():
        print(f'La carpeta {ruta} no existe')
        return
    
    print(f'Buscando patrones en {ruta}')
    paths = obtener_ficheros(ruta, args.target)
    detecciones = [detectar_patrones(path) for path in paths]
    # lista de listas a lista
    detecciones = [d for deteccion in detecciones for d in deteccion]
    detecciones.insert(0, ("Fichero", "Patrón", "Detección", "Linea", "Posición", "Fragmento"))

    # Cálculo de la longitud máxima de cada columna
    max_l = [max([len(str(d[i]))+2 for d in detecciones]) for i in range(len(detecciones[0]))]

    # Imprimir tabla
    print("="*sum(max_l))
    print(f"{detecciones[0][0]:<{max_l[0]}}{detecciones[0][1]:<{max_l[1]}}{detecciones[0][2]:<{max_l[2]}}{detecciones[0][3]:<{max_l[3]}}{detecciones[0][4]:<{max_l[4]}}{detecciones[0][5]:<{max_l[5]}}")
    print("="*sum(max_l))
    tmp = detecciones[1][0]
    for d in detecciones[1:]:
        if d[0] != tmp:
            print("-"*sum(max_l))
        tmp = d[0]
        print(f"{d[0]:<{max_l[0]}}{d[1]:<{max_l[1]}}{d[2]:<{max_l[2]}}{d[3]:<{max_l[3]}}{d[4]:<{max_l[4]}}{d[5]:<{max_l[5]}}")

if __name__ == '__main__':
    main()