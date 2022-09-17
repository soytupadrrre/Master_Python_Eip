from dataclasses import dataclass
from typing import List, Optional, Union
import pymongo
from datetime import datetime
from argparse import ArgumentParser
from tabulate import tabulate

@dataclass
class Nota:
    """
    Clase que representa una nota de un alumno

    :param nombre: Nombre del alumno
    :type nombre: str
    :param edad: Edad del alumno
    :type edad: int
    :param email: Email del alumno
    :type email: str
    :param nota: Nota del alumno
    :type nota: int
    :param fecha: Fecha de la nota, default datetime.today().replace(microsecond=0)
    :type fecha: datetime
    :param _id: Identificador de la nota, default None
    :type _id: Optional[str]


    :return: _description_
    :rtype: _type_
    """
    nombre: str
    edad: int
    email: str
    nota: float
    fecha: datetime = datetime.today().replace(microsecond=0)
    _id: Optional[str] = None

    def to_insert(self) -> dict:
        """
        Método que devuelve un diccionario con los atributos de la nota, para insertar en la base de datos MongoDB

        :return: Diccionario con los atributos de la nota
        :rtype: dict
        """
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "email": self.email,
            "nota": self.nota,
            "fecha": self.fecha
        }

    def get_as_dict(self, attr) -> dict:
        """
        Método que devuelve un diccionario con un atributo del objeto

        :param attr: Atributo del objeto
        :type attr: str

        :return: Diccionario con el atributo del objeto
        :rtype: dict
        """
        return {attr: getattr(self, attr)}

class Database:
    """
    Clase que representa una base de datos MongoDB

    :param uri: URI de la base de datos
    :type uri: str
    :param database: Nombre de la base de datos
    :type database: str
    :param collection: Nombre de la colección
    :type collection: str
    """
    def __init__(self, uri: str, database: str, collection: str):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def insert(self, nota: Nota) -> str:
        """
        Método que inserta una nota en la base de datos

        :param nota: Nota a insertar
        :type nota: Nota
        :return: ID de la nota insertada
        :rtype: str
        """
        result = self.collection.insert_one(nota.to_insert())
        return result.inserted_id

    def find_many(self, **kwargs) -> List[Nota]:
        """
        Método que devuelve una lista de notas que cumplan con los criterios de búsqueda

        :return: Lista de notas
        :rtype: List[Nota]
        """
        return [Nota(**x) for x in self.collection.find(kwargs)]

    def find_all(self) -> List[Nota]:
        """
        Método que devuelve una lista de todas las notas

        :return: Lista de notas
        :rtype: List[Nota]
        """
        return [Nota(**x) for x in self.collection.find()]

    def update(self, filter_by: dict, update: dict) -> int:
        """
        Método que actualiza una nota

        :param filter_by: Criterio de búsqueda
        :type filter_by: dict
        :param update: Criterio de actualización
        :type update: dict
        :return: Número de notas actualizadas
        :rtype: int
        """
        count = self.collection.update_one(filter_by, {"$set": update})
        return count.modified_count

    def delete(self, **kwargs) -> int:
        """
        Método que elimina una nota
            
        :return: Número de notas eliminadas
        :rtype: int
        """
        deleted = self.collection.delete_one(kwargs)
        return deleted.deleted_count

    def close(self):
        """
        Método que cierra la conexión con la base de datos
        """
        self.client.close()


def apartado_1(database: Database, lista_notas: List[Nota]):
    try:
        for nota in lista_notas:
            inserted_id = database.insert(nota)
            print(f"Insertado notas de {nota.nombre} con id {inserted_id}")
    except Exception as e:
        print(f"Error al insertar {nota}: {e}")

def apartado_2(database: Database, filter_by: dict, update_dict: dict):
    try:
        updated = database.update(filter_by, update_dict)
        print(f"Actualizados {updated} notas con {filter_by}")
    except Exception as e:
        print(f"Error al actualizar: {e}")

def apartado_3(database: Database):
    try:
        results = database.find_all()
        notas = [x.__dict__ for x in results]
        for nota in notas:
            nota["fecha"] = nota["fecha"].strftime("%d-%m-%Y %H:%M:%S")
        print("Colección de notas:")
        print(tabulate(notas, headers="keys", tablefmt="psql"))
    except Exception as e:
        print(f"Error al buscar: {e}")

def apartado_4(database: Database, start: Union[int, float], end: Union[int, float]):
    try:
        results = database.find_many(nota={"$gte": start, "$lte": end})
        notas = [x.__dict__ for x in results]
        for nota in notas:
            nota["fecha"] = nota["fecha"].strftime("%d-%m-%Y %H:%M:%S")
        print(f"Notas entre {start} y {end}:")
        print(tabulate(notas, headers="keys", tablefmt="psql"))
    except Exception as e:
        print(f"Error al buscar: {e}")

def apartado_5(database: Database, delete_dict: dict):
    try:
        count = database.delete(**delete_dict)
        print(f"Borrados {count} documentos con {delete_dict}")
    except Exception as e:
        print(f"Error al borrar {delete_dict}: {e}")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-a", "--apartado", required=True, type=int, help="Apartado a ejecutar", choices=[1, 2, 3, 4, 5])
    parser.add_argument("-hn", "--hostname", default="root:root@localhost")
    parser.add_argument("-p", "--port", default=27017)
    parser.add_argument("-d", "--database", default="actividad")
    parser.add_argument("-c", "--collection", default="notas")
    args = parser.parse_args()

    database = Database(f"mongodb://{args.hostname}:{args.port}", args.database, args.collection)

    nota_pedro = Nota("Pedro López", 25, "pedro@eip.com", 5.2)
    nota_julia = Nota("Julia García", 22, "julia@eip.com", 7.3)
    nota_amparo = Nota("Amparo Mayoral", 28, "amparao@eip.com", 8.4)
    nota_juan = Nota("Juan Martínez", 30, "juan@eip.com", 6.8)

    if args.apartado == 1:
        apartado_1(database, [nota_pedro, nota_julia, nota_amparo, nota_juan])
    elif args.apartado == 2:
        nota_amparo.nota = 9.3
        nota_juan.nota = 7.2

        for nota in [nota_amparo, nota_juan]:
            apartado_2(database, nota.get_as_dict("nombre"), nota.get_as_dict("nota"))
        
    elif args.apartado == 3:
        apartado_3(database)
    elif args.apartado == 4:
        apartado_4(database, start=7, end=7.5)
    elif args.apartado == 5:
        apartado_5(database, nota_pedro.get_as_dict("nombre"))

    database.close()