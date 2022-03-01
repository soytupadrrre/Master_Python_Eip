import os
FILE_PATH = os.path.join(os.path.dirname(__file__), "fichero.txt")

def main():
    """
    Funcion principal
    """
    # Crear un fichero
    fichero = open(FILE_PATH, "w")
    fichero.write("Hola\n")
    fichero.write("Mundo\n")
    fichero.write("Adios\n")
    fichero.close()

    # Leer el fichero
    fichero = open(FILE_PATH, "r")
    
    # Mostrar el contenido del fichero
    print(fichero.read())

if __name__ == "__main__":
    main()
