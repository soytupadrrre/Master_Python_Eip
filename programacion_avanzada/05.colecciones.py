"""
Almacenar números del 1 al 10 en una lista utilizando un bucle while. Mostrar la lista en orden inverso
Crear un diccionario con 4 valores (mostrarlo), modificar el tercer valor, añadir un nuevlo valor de tipo lista y mostrarlo

Script creado para la asignatura de Programación Avanzada en Python de la Escuela Internacional de Postgrados

Uso: 
- Windows: python colecciones.py
- Linux: python3 coleciones.py

@autor: Víctor Luque Martín
@fecha: 27-02-2022
@versión: 1.0
@licencia: MIT
@email: victorluque341@gmail.com
"""

def rellenar_lista():
    lista = []
    i = 1
    while i <= 10:
        lista.append(i)
        i += 1
    return lista

def uso_de_diccionario():
    diccionario = {
        "nombre": "Víctor",
        "apellidos": "Luque Martín",
        "edad": "20",
        "direccion": "C/ Calle imaginaria, 4"
    }
    original = diccionario.copy()
    diccionario["edad"] = "21"
    diccionario["amigos"] = ["Juan", "Pedro", "Luis", "Carlos"]
    return original, diccionario

if __name__ == "__main__":
    print("\n======== Lista ========")
    lista = rellenar_lista()
    print("Lista normal: ", lista)
    lista.reverse()
    print("Lista inversa: ", lista)
    print("=======================")
    print("\n===== Diccionario =====")
    diccionario_original, diccionaro_modificado = uso_de_diccionario()
    print("Diccionario original: ", diccionario_original)
    print("Diccionario modificado: ", diccionaro_modificado)
    print("=======================")