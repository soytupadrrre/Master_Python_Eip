# Create a CRUD application using Python and PostgreSQL
from dataclasses import dataclass
from typing import List, Union
import psycopg2
from tabulate import tabulate
from argparse import ArgumentParser

@dataclass
class Edicion:
    id_edic: int
    numero: str

@dataclass
class Nota:
    id_notas: int
    name: str
    edad: int
    nota: float
    id_edic: Edicion

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            user = "postgres",
            password = "postgres",
            host = "localhost",
            port = "5432",
            database = "actividad"
        )
        self.cursor = self.connection.cursor()
        print("Connected to PostgreSQL server")

    def insert_edicion(self, edicion: Edicion):
        try:
            self.cursor.execute("INSERT INTO edicion (numero) VALUES (%s)", (edicion.numero,))
            self.connection.commit()
            print(f"Edicion '{edicion.numero}' insertada correctamente")
        except Exception as e:
            print(e)

    def insert_notas(self, notas: Nota):
        try:
            self.cursor.execute(
                'INSERT INTO notas ("name", "edad", "notas", "ID edic") VALUES (%s, %s, %s, %s)', 
                (notas.name, notas.edad, notas.nota, notas.id_edic.id_edic)
            )
            self.connection.commit()
            print(f"Notas de {notas.name} insertadas correctamente")
        except Exception as e:
            print(e)

    def select_edicion(self) -> List[Edicion]:
        try:
            self.cursor.execute("SELECT * FROM edicion")
            edicion = self.cursor.fetchall()
            return [Edicion(id_edic = row[0], numero = row[1]) for row in edicion]
        except Exception as e:
            print(e)

    def select_notas(self) -> List[Nota]:
        try:
            # use joins
            self.cursor.execute('SELECT * FROM notas INNER JOIN edicion ON edicion."ID edic" = notas."ID edic"')
            notas = self.cursor.fetchall()
            lista_notas = []
            for nota in notas:
                lista_notas.append(
                    Nota(
                        id_notas = nota[0], 
                        name = nota[1], 
                        edad = nota[2], 
                        nota = nota[3], 
                        id_edic = Edicion(
                            id_edic = nota[4], 
                            numero = nota[5])
                    )
                )

            return lista_notas
        except Exception as e:
            print(e)

    def select_notas_where_edicion_is(self, numero: str) -> List[Nota]:
        try:
            # use joins
            self.cursor.execute('SELECT * FROM notas INNER JOIN edicion ON notas."ID edic" = edicion."ID edic" WHERE edicion.numero = %s', (numero,))
            notas = self.cursor.fetchall()
            lista_notas = []
            for nota in notas:
                lista_notas.append(
                    Nota(
                        id_notas = nota[0], 
                        name = nota[1], 
                        edad = nota[2], 
                        nota = nota[3], 
                        id_edic = Edicion(
                            id_edic = nota[4], 
                            numero = nota[5])
                    )
                )

            return lista_notas
        except Exception as e:
            print(e)

    def select_notas_btw(self, start, end) -> List[Nota]:
        try:
            self.cursor.execute('SELECT * FROM notas INNER JOIN edicion ON edicion."ID edic" = notas."ID edic" WHERE notas.notas BETWEEN %s AND %s', (start, end))
            notas = self.cursor.fetchall()
            lista_notas = []
            for nota in notas:
                lista_notas.append(
                    Nota(
                        id_notas = nota[0], 
                        name = nota[1], 
                        edad = nota[2], 
                        nota = nota[3], 
                        id_edic = Edicion(
                            id_edic = nota[4], 
                            numero = nota[5])
                    )
                )

            return lista_notas
        except Exception as e:
            print(e)

    def update_notas(self, notas: Nota):
        try:
            self.cursor.execute('UPDATE notas SET name = %s, edad = %s, notas = %s, "ID edic" = %s WHERE "ID notas" = %s', (notas.name, notas.edad, notas.nota, notas.id_edic.id_edic, notas.id_notas))
            self.connection.commit()
            print(f"Notas de {notas.name} actualizadas correctamente")
        except Exception as e:
            print(e)

    def delete_notas_by_name(self, name: str):
        try:
            self.cursor.execute("DELETE FROM notas WHERE name = %s", (name,))
            self.connection.commit()
            print(f"Notas de {name} eliminadas correctamente")
        except Exception as e:
            print(e)


def apartado_1(database: Database, ediciones: List[Edicion], notas: List[Nota]):
    for edicion in ediciones:
        database.insert_edicion(edicion)

    for nota in notas:
        database.insert_notas(nota)

def apartado_2(database: Database, new_nota: Nota):
    # update
    database.update_notas(new_nota)

def apartado_3(database: Database):
    # select
    ediciones = [x.__dict__ for x in database.select_edicion()]
    print("Tabla edicion")
    print(tabulate(ediciones, headers="keys", tablefmt="grid"))
    notas = [x.__dict__ for x in database.select_notas()]
    print("Tabla notas")
    print(tabulate(notas, headers="keys", tablefmt="grid"))

def apartado_4(database: Database, start: Union[int, float], end: Union[int, float]):
    # select
    notas = [x.__dict__ for x in database.select_notas_btw(start, end)]
    print(f"Tabla notas entre {start} y {end}")
    print(tabulate(notas, headers="keys", tablefmt="grid"))

def apartado_5(database: Database, num_edicion: str):
    # select
    notas = database.select_notas_where_edicion_is(num_edicion)
    notas = [x.__dict__ for x in notas]
    print(f"Tabla notas de la edicion numero '{num_edicion}'")
    print(tabulate(notas, headers="keys", tablefmt="grid"))

def apartado_6(database: Database, name: str):
    # delete
    database.delete_notas_by_name(name)

if __name__ == "__main__":
    database = Database()
    parser = ArgumentParser()
    parser.add_argument("-a", "--apartado", type=int, required=True, help="Apartado a ejecutar", choices=[1, 2, 3, 4, 5, 6])
    args = parser.parse_args()

    edicion_1 = Edicion(id_edic = 1, numero = "uno")
    edicion_2 = Edicion(id_edic = 2, numero = "dos")
    edicion_3 = Edicion(id_edic = 3, numero = "tres")

    nota_isabel = Nota(id_notas= 1, name = "Isabel Maniega", edad = 30, nota = 5.6, id_edic = edicion_1)
    nota_jose = Nota(id_notas= 2, name = "José Manuel Peña", edad = 30, nota = 7.8, id_edic = edicion_1)
    nota_pedro = Nota(id_notas= 3, name = "Pedro López", edad = 25, nota = 5.2, id_edic = edicion_2)
    nota_julia = Nota(id_notas= 4, name = "Julia García", edad = 22, nota = 7.3, id_edic = edicion_1)
    nota_amparo = Nota(id_notas= 5, name = "Amparo Mayora", edad = 28, nota = 8.4, id_edic = edicion_3)
    nota_juan = Nota(id_notas= 6, name = "Juan Martínez", edad = 30, nota = 6.8, id_edic = edicion_3)
    nota_fernando = Nota(id_notas= 7, name = "Fernando López", edad = 35, nota = 6.1, id_edic = edicion_2)
    nota_maria = Nota(id_notas= 8, name = "María Castro", edad = 41, nota = 5.9, id_edic = edicion_3)

    if args.apartado == 1:
        lista_ediciones = [edicion_1, edicion_2, edicion_3]
        lista_notas = [nota_isabel, nota_jose, nota_pedro, nota_julia, nota_amparo, nota_juan, nota_fernando, nota_maria]
        apartado_1(database, lista_ediciones, lista_notas)

    elif args.apartado == 2:
        new_pedro = Nota(**nota_pedro.__dict__)
        new_pedro.nota = 6.4
        new_maria = Nota(**nota_maria.__dict__)
        new_maria.nota = 5.2
        apartado_2(database, new_pedro)
        apartado_2(database, new_maria)
    
    elif args.apartado == 3:
        apartado_3(database)

    elif args.apartado == 4:
        apartado_4(database, 5, 6.5)

    elif args.apartado == 5:
        apartado_5(database, "dos")

    elif args.apartado == 6:
        apartado_6(database, "Pedro López")


    

    
        