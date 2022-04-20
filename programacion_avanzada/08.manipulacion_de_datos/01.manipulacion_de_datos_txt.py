"""
Manipulación de datos, trabajando con ficheros TXT

Script creado para la asignatura de Programación Avanzada en Python de la Escuela Internacional de Postgrados

Uso: 
- Windows: python "08.manipulacion_de_datos/01.manipulacion_de_datos_txt.py"
- Linux: python3 "08.manipulacion_de_datos/01.manipulacion_de_datos_txt.py"

@autor: Víctor Luque Martín
@fecha: 04-03-2022
@versión: 1.0
@licencia: MIT
@email: victorluque341@gmail.com
"""
import os
FILE_PATH = os.path.join(os.path.dirname(__file__), "fichero.txt")

def main():
    """
    Funcion principal
    """
    # Crear un fichero
    fichero = open(FILE_PATH, "w")
    # Escribir en el fichero
    fichero.write("Hola\n")
    fichero.write("Mundo\n")
    fichero.write("Adios\n\n")
    # Cerrar fichero
    fichero.close()

    # Método with open
    # Actualización de fichero
    with open(FILE_PATH, "a") as fichero:
        fichero.writelines([
            "Hola2\n", "Mundo2\n",
            "Esto lo he escrito\n", 
            "con 'with open'"
        ])

    # Leer el fichero
    fichero = open(FILE_PATH, "r")
    
    # Mostrar el contenido del fichero
    print(fichero.read())

if __name__ == "__main__":
    main()
