#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Mostrar numeros enternos de 0 a un numero introducido por el usuario
Mostrar valores de un diccionario

Script creado para la asignatura de Programación Avanzada en Python de la Escuela Internacional de Postgrados

Uso: 
- Windows: python "bucles.py"
- Linux: python3 "bucles.py"

@autor: Víctor Luque Martín
@fecha: 27-02-2022
@versión: 1.0
@licencia: MIT
@email: victorluque341@gmail.com
"""

def mostrar_numeros(numero:int) -> None:
    for i in range(numero+1):
        print("- ", i)

def mostrar_valores_diccionario() -> None:
    diccionario_contactos = {
        "pepe": "pepe@mail.com",
        "carlos": 111222333,
        "juan": ["juan@mail.com", 444555666]
    }
    # Bucle para recorrer los valores del diccionario
    for value in diccionario_contactos.values():
        print(value) 

if __name__ == "__main__":
    print(f"\n===== Mostrar números =====")
    try:
        numero = int(input("Introduce un número entero: "))
    except:
        print("El valor introducido no es un número entero")
    
    print(f"Números enteros del 0 al {numero}:")
    mostrar_numeros(numero)
    print("===== Fin mostrar números =====")
    print("")
    print("===== Mostrar valores de diccionario =====")
    mostrar_valores_diccionario()
    print("===== Fin mostrar valores de diccionario =====\n")