"""
Suma y resta de dos números, uso de excepciones para controlar errores.
Recursividad de la suma de los n primeros números.

Script creado para la asignatura de Programación Avanzada en Python de la Escuela Internacional de Postgrados

Uso: 
- Windows: python Luque_Martín_Víctor_Actividad_3.py
- Linux: python3 Luque_Martín_Víctor_Actividad_3.py

@autor: Víctor Luque Martín
@fecha: 27-02-2022
@versión: 1.0
@licencia: MIT
@email: victorluque341@gmail.com
"""
def sumar_y_restar(a:int or float, b:int or float) -> tuple:
    """
    Suma y resta dos números enteros o flotantes

    :param a: primer número
    :type a: int or float
    :param b: segundo número
    :type b: int or float
    :return: suma y resta de los dos números
    :rtype: tuple
    """
    suma = None
    resta = None
    try:
        if isinstance(a, float) and isinstance(b, float) or \
            isinstance(a, int) and isinstance(b, int):
            suma, resta = a + b, a - b
        else:
            raise TypeError("Los valores deben ser números")
    except TypeError as e:
        print(e)
    
    finally:
        return suma, resta

def calc_suma_recursiva(n:int=10) -> int:
    """
    Calcula la suma recursiva de los n primeros números
    Valor predefinido: 10

    :param n: número de números a sumar
    :type n: int
    :return: suma de los n primeros números
    :rtype: int
    """
    if n == 0:
        return 0
    else:
        return n + calc_suma_recursiva(n-1)

if __name__ == "__main__":
    print("\n===== Suma y resta =====")
    a, b = 10, 5
    suma, resta = sumar_y_restar(a, b)
    print(f"La suma de {a} y {b} es {suma} y la resta es {resta}")
    a, b = 40, 20
    suma, resta = sumar_y_restar(a, b)
    print(f"La suma de {a} y {b} es {suma} y la resta es {resta}")
    a, b = 0.4, 2.6
    suma, resta = sumar_y_restar(a, b)
    print(f"La suma de {a} y {b} es {suma} y la resta es {resta}")
    """ 
    Test error
    a, b = "test_string", "test_error"
    suma, resta = sumar_y_restar(a, b)
    print(f"La suma de {a} y {b} es {suma} y la resta es {resta}") 
    """
    print("===== Fin Suma y Resta =====")

    print("\n===== Suma recursiva =====")
    numero_suma_recursiva = 10
    suma_recursiva = calc_suma_recursiva(numero_suma_recursiva)
    print(f"La suma recursiva de los {numero_suma_recursiva} primeros números es {suma_recursiva}")
    print("===== Fin Suma recursiva =====\n")