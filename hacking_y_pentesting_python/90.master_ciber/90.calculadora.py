import sys

# Objeto Calculadora
class Calculadora:

    # Inicialización
    def __init__(self, number:int or float) -> None:
        self.a:int or float = number

     # Método privado: Suma
    def __suma(self, b:int or float) -> int or float:
         return self.a + b
 
     # Método privado: Resta
    def __resta(self, b:int or float) -> int or float:
        return self.a - b

    # Método privado: Producto
    def __producto(self, b:int or float) -> int or float:
        return self.a * b

    # Método privado: División
    def __division(self, b:int or float) -> int or float:
        return self.a / b

    # Método público: Funciones de la calculadora, en base a opciones dadas por el usuario
    def calculadora(self, choice:str, b:int or float) -> int or float:
        
        if choice == "1":
            return self.__suma(b)

        elif choice == "2":
            return self.__resta(b)
        
        elif choice == "3":
            return self.__producto(b)
        
        elif choice == "4":
            return self.__division(b)

        else:
            print("Opcion incorrecta")

    # Método público: Recuperar opciones del menú de la calculadora / Cerrar el programa en caso de que la opción sea 0
    def switch(self, choice:str) -> str or bool:
        if choice in ["1", "2","3","4","5"]:
            return choice
        elif choice =="0":
            sys.exit()
        else:
            return False

    # Método público: Menu de la calculadora
    def menu(self):
        print("\nIndique la operación")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Restablecer") 
        print("0. Salir\n") 
        return self.switch(input())

if __name__ == "__main__":
    try:
        # Introducir primer valor
        num1 = input("Introduzca un valor\n")
        
        # Crear el objeto calculadora
        calculadora = Calculadora(float(num1))

        # Bucle para hacer múltiples operaciones
        while True:

            # Imprimir el menú de la calculadora y recuperar la opción elegida
            choice = calculadora.menu()

            # En caso de que la opción sea 5, restablece la calculadora y se solicita un nuevo número
            if choice == "5":
                num2 = input("Introduzca un valor nuevo\n")
                calculadora = Calculadora(float(num2))

            # En caso de escoger una opción no existente se exige al usuario que elija una opción válida
            elif not choice:
                print("\nElija una de las opciones disponibles\n")

            else:
                
                # Solicitar segundo valor para realizar la operación matemática
                num2 = input("Introduzca el siguiente valor\n")
                
                # Lista de simbolos para mejorar la salifa por consola
                symbols = ["+", "-", "*", "/"]
                
                # Obtención del resultado de la operación matemática a través de una opción y el segundo valor
                result = calculadora.calculadora(choice, float(num2))
                
                # Impresión por pantalla de la solución: Resultado: 1.0 + 2.0 = 3.0
                print("\nResultado: "+str(calculadora.a)+" "+ symbols[int(choice)-1] +" "+str(float(num2))+" = " + str(result) + "\n")

                # Actualizar la calculadora con el valor resultante para hacer múltiples operaciones concatenadas
                calculadora = Calculadora(float(result))

    # Omisión de Error al pulsar Crtl + C (Salir del programa)
    except KeyboardInterrupt:
        sys.exit()