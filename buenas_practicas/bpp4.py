"""
Depuración y reglas de optimización de código

Script creado para la asignatura de Buenas Prácticas de Programación en Python de la Escuela Internacional de Postgrados.

@autor: Víctor Luque Martín
@fecha: 30-06-2022
@versión: 1.0
@licencia: MIT
@email: victorluque341@gmail.com
"""
from typing import List, Tuple
import pdb
#pdb.set_trace()

bold = '\033[1m'
reset = '\033[0m'

def get_max_of_list_of_sublist(list_of_sublist: List[List[int]]) -> List[Tuple[int]]:
    """
    Devuelve una lista de tuplas con el indice de la sublista el elemento más grande de cada sublista y su posicion

    :param list_of_sublist: List of lists of ints
    :type list_of_sublist: List[List[int]]
    :return: Lista de tuplas de enteros
    :rtype: List[Tuple[int]]
    """
    list_compression = [(list_of_sublist.index(sublist), sublist.index(max(sublist)), max(sublist)) for sublist in list_of_sublist]
    return list_compression

def is_prime(number: int) -> bool:
    """
    Devuelve True si el numero es primo

    :param number: Numero entero
    :type number: int
    :return: True si el numero es primo, False si no lo es
    :rtype: bool
    """
    if number == 1 or number == 0:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def filter_prime_numbers(numbers: List[int]) -> List[int]:
    """
    Devuelve una lista de enteros con los numeros primos

    :param numbers: Lista de enteros
    :type numbers: List[int]
    :return: Lista de enteros con los numeros primos
    :rtype: List[int]
    """
    return list(filter(is_prime, numbers))

def print_table(max_items: List[List[str]]) -> None:
    """
    Imprime una tabla de texto

    :param table: Tabla de texto
    :type table: List[List[str]]
    :return: None
    :rtype: None
    """
    title_sublist = "Nº Sublista"
    title_position = "Posicion"
    title_max_item = "Valor Máximo"
    header = f" | {bold}{title_sublist:^12}{reset} | {bold}{title_position:^12}{reset} | {bold}{title_max_item:^10}{reset} | "
    line = " " + "+" + "-"*14 + "+" + "-"*14 + "+" + "-"*14 + "+" 
    print(line)
    print(header)
    print(line.replace("-", "="))
    for item in max_items:
        msg_sublist = f"{bold}{item[0]}{reset}"
        msg_position = f"{bold}{item[1]}{reset}"
        msg_max = f"{bold}{item[2]}{reset}"
        row = f" | {msg_sublist:^20} | {msg_position:^20} | {msg_max:^20} |"
        print(row)
        print(line)

if __name__ == "__main__":
    msg = " Máximo de sublistas "
    print(f"\n{msg:=^80}", end="\n\n")
    list_of_lists = [[2,4,1], [1,2,3,4,5,6,7,8], [100,250,43]]
    print(f"Lista de listas: {list_of_lists}\n")
    max_items = get_max_of_list_of_sublist(list_of_lists)
    print_table(max_items)
    print("")
    msg = " Numeros primos "
    print(f"{msg:=^80}", end="\n\n")
    primos_a_comprobar = [3,4,8,5,5,22,13]
    primos = filter_prime_numbers(primos_a_comprobar)
    print(f"De los {len(primos_a_comprobar)} numeros {*primos_a_comprobar,}, hay un total de {len(primos)} primos {*primos,}\n")
    msg = " FIN "
    print(f"{msg:=^80}", end="\n\n")

