"""
Creación de clase Calculadora que contiene los métodos suma, resta, multiplicación y división.

Script creado para la asignatura de Programación Avanzada en Python de la Escuela Internacional de Postgrados

Uso: 
- Windows: python Luque_Martín_Víctor_Actividad_4.py
- Linux: python3 Luque_Martín_Víctor_Actividad_4.py

@autor: Víctor Luque Martín
@fecha: 27-02-2022
@versión: 1.0
@licencia: MIT
@email: victorluque341@gmail.com
"""
# Objeto Calculadora
class Calculadora:

    # Inicialización
    def __init__(self, num_1:int or float, num_2:int or float) -> None:
        self.num_1 = num_1
        self.num_2 = num_2

     # Método público: Suma
    def suma(self) -> int or float:
         return self.num_1 + self.num_2
 
     # Método público: Resta
    def resta(self) -> int or float:
        return self.num_1 - self.num_2

    # Método público: Producto
    def multiplicar(self) -> int or float:
        return self.num_1 * self.num_2

    # Método público: División
    def division(self) -> int or float:
        return self.num_1 / self.num_2


if __name__ == "__main__":
    num_1, num_2 = 10, 5
    calculadora = Calculadora(num_1, num_2)
    print("=== Calculadora ===")
    print(f"Suma: {num_1} + {num_2} = {calculadora.suma()}")
    print(f"Resta: {num_1} - {num_2} = {calculadora.resta()}")
    print(f"Multiplicación: {num_1} * {num_2} = {calculadora.multiplicar()}")
    print(f"División: {num_1} / {num_2} = {calculadora.division()}")
    print("===================")