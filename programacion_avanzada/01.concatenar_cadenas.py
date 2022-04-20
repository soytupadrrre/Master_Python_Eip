"""
Concatenar cadenas de texto en python

Script creado para la asignatura de Programación Avanzada en Python de la Escuela Internacional de Postgrados

Uso: 
- Windows: python "concatenar_cadenas.py"
- Linux: python3 "concatenar_cadenas.py"

@autor: Víctor Luque Martín
@fecha: 27-02-2022
@versión: 1.0
@licencia: MIT
@email: victorluque341@gmail.com
"""
def main() -> None:
    """
    Función principal

    Concatenar cadenas de texto y mostrar su longitud

    Posibles opciones:
    1. Uso del operador +
        - cadena_concatenada = cadena_1 + cadena_2
    2. Uso de función concat de la librería operator
        - from operator import concat
        - cadena_concatenada = concat(cadena_1, cadena_2)
    3. Formatos de cadenas (Función Format, F-String, Operador %)
        - cadena_concatenada = '{}{}'.format(cadena_1, cadena_2)
        - cadena_concatenada = f'{cadena_1}{cadena_2}'
        - cadena_concatenada = '%s%s' % (cadena_1, cadena_2)
    4. Creación de lista de cadenas y uso de función join
        - cadena_concatenada = ''.join([cadena_1, cadena_2])
    """
    cadena_1 = str(input("Introduce una cadena de texto: "))
    cadena_2 = str(input("Introduce otra cadena de texto: "))
    # from operator import concat
    cadena_concatenada = cadena_1 + cadena_2
    logitud_cadena = len(cadena_concatenada)
    print("La cadena concatenada es: ", cadena_concatenada)
    print("La longitud de la cadena concatenada es: ", logitud_cadena)

if __name__ == "__main__":
    main()