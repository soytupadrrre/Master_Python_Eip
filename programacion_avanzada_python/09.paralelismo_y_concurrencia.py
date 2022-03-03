#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Trabajar con hilos

Script creado para la asignatura de Programación Avanzada en Python de la Escuela Internacional de Postgrados

Uso: 
- Windows: python "09.paralelismo_y_concurrencia.py"
- Linux: python3 "09.paralelismo_y_concurrencia.py"

@autor: Víctor Luque Martín
@fecha: 27-02-2022
@versión: 1.0
@licencia: MIT
@email: victorluque341@gmail.com
"""
import threading
import time
from datetime import datetime

def thread_task(thread_id):
    """
    Función que se ejecuta en cada hilo
    """
    start_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(f"El hilo {thread_id} inicio a las {start_time}")
    time.sleep(1)
    end_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(f"El hilo {thread_id} termino a las {end_time}")

def main():
    """
    Funcion principal
    """
    print("Inicio del programa")
    # Crear una lista de hilos
    threads = []
    for i in range(1, 10):
        # Crear un hilo
        t = threading.Thread(target=thread_task, args=(i,))
        # Arrancar el hilo
        t.start()
        # Añadir el hilo a la lista
        threads.append(t)

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()
    print("El programa ha terminado")

if __name__ == '__main__':
    main()