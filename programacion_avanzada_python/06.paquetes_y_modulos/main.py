"""
Trabajando con paquetes y modulos. Crea un paquete con la siguiente estructura:
- main.py
- paquete
    - subpaquete_1
        - mod1.py
        - mod2.py
    - subpaquete_2
        - mod3.py
        - mod4.py

Añade una función print que muestre los nombres de los módulos del paquete.
Importa el paquete y llama a los diferentes módulos.


Script creado para la asignatura de Programación Avanzada en Python de la Escuela Internacional de Postgrados

Uso: 
- Windows: python "main.py"
- Linux: python3 "main.py"

@autor: Víctor Luque Martín
@fecha: 28-02-2022
@versión: 1.1
@licencia: MIT
@email: victorluque341@gmail.com
"""
from package.sub_package1.mod1 import module_name as mod1
from package.sub_package1.mod2 import module_name as mod2
from package.sub_package2.mod3 import module_name as mod3
from package.sub_package2.mod4 import module_name as mod4

if __name__ == "__main__":
    mod1()
    mod2()
    mod3()
    mod4()