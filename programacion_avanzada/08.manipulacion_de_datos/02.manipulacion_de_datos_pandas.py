"""
Manipulación de datos, trabajando con PANDAS

Script creado para la asignatura de Programación Avanzada en Python de la Escuela Internacional de Postgrados

Uso: 
- Windows: python "08.manipulacion_de_datos/02.manipulacion_de_datos_pandas.py"
- Linux: python3 "08.manipulacion_de_datos/02.manipulacion_de_datos_pandas.py"

@autor: Víctor Luque Martín
@fecha: 04-03-2022
@versión: 1.0
@licencia: MIT
@email: victorluque341@gmail.com
"""
import pandas as pd
import os
import matplotlib.pyplot as plt

# Path absoluto del fichero cotización csv (evitar errores, situado al mismo nivel que fichero python)
FILE_PATH = os.path.join(os.path.dirname(__file__), "cotizacion.csv")

def main():
    """
    Función principal

    Lectura de CSV con pandas, delimitador decimal es "," y el delimitador de columna es ";"
    Nota:
    - Se ha modificado la estructura de los datos contenidos en cotizacion.csv en la columna "Volumen"
      los "." para indicar "miles" para que la librería pandas interpretara los valores como int o float64

    - Se ha intentado incluir el parámetro 'thousands=r"."' para su posible interpretación pero no ha solucionado
      el error de interpretación de los datos, tratandolos como un "object" en vez de "float64".

    - Se ha incluido la librería matploitlib para interpretar los datos de forma gráfica.
    """
    # Lectura de fichero CSV
    df:pd.DataFrame = pd.read_csv(FILE_PATH, delimiter=";", decimal=",", index_col="Nombre")

    # Calcular minimo, máximo y media de cada columna
    minimo, maximo, media = df.min(), df.max(), df.mean()

    # Mostrar los datos redondeados (3 decimales)
    print("\n========== MINIMOS ==========")
    print(minimo.round(3))
    print("=============================")
    print("\n========== MAXIMOS ==========")
    print("MAXIMOS")
    print(maximo.round(3))
    print("=============================")
    print("\n========== MEDIA ==========")
    print("MEDIAS")
    print(media.round(3))
    print("===========================\n")

    # Mostrar graficamente
    minimo.plot(title="Minimo")
    plt.show()
    maximo.plot(title="Maximo")
    plt.show()
    media.plot(title="Media")
    plt.show()

if __name__ == "__main__":
    main()