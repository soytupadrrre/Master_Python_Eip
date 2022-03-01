"""
Trabajando con Bases de Datos

Script creado para la asignatura de Programación Avanzada en Python de la Escuela Internacional de Postgrados

Descripción:
- Creación de clase "Crud" para manejar la conexión a la base de datos
- Datos de prueba

Notas:
- La función main se situa al final del script
- Es necesario descomentar (en caso de que lo estén) las líneas de código que se encuentran en la función main para que funcione

Uso: 
- Windows: python "base_de_datos.py"
- Linux: python3 "base_de_datos.py"

@autor: Víctor Luque Martín
@fecha: 01-03-2022
@versión: 1.0
@licencia: MIT
@email: victorluque341@gmail.com
"""
import os
import sqlite3
from sqlite3 import Error

# Obtención de la ruta del archivo de la base de datos en el mismo directorio que el script
DB_FILE = os.path.join(os.path.dirname(__file__), "database.db")

class Crud():
    """
    Clase que permite crear, leer, actualizar y borrar registros en una base de datos SQLite.
    """
    def __init__(self, db_file) -> None:
        """
        Inicializar la conexión con la base de datos
        
        :param db_file: nombre del archivo de la base de datos
        """
        self.db_file = db_file
        self.conn = self.create_connection()

    # ================ Crear una base de datos ================
    def create_connection(self):
        """
        Creación de la conexión a la base de datos

        :return: Objeto de conexión
        """
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(e)

    # ================== Crear una tabla =====================
    def create_table(self, create_table_sql):
        """ 
        Creación de una tabla en la base de datos desde una cadena SQL

        :param create_table_sql: sentencia SQL para crear la tabla
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    # ================== INSERT =====================
    def insert_user(self, user):
        """
        Creación de un nuevo usuario

        :param user: detalles del usuario como una tupla
        :return: id del usuario
        """
        sql = ''' INSERT INTO users(username, email, age, password) VALUES(?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, user)
        self.conn.commit()
        return cur.lastrowid

    def insert_company(self, company):
        """
        Creación de una nueva empresa

        :param company: detalles de la empresa como una tupla
        :return: id de la empresa
        """
        sql = ''' INSERT INTO companies(name, description) VALUES(?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, company)
        self.conn.commit()
        return cur.lastrowid

    # ================== UPDATE =====================
    def update_user(self, user):
        """
        Actualizar un usuario en la base de datos

        :param user: detalles del usuario como una tupla
        :return: id del usuario
        """
        sql = ''' UPDATE users SET username = ?, email = ?, age = ?, password = ? WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql, user)
        self.conn.commit()
        return cur.lastrowid

    def update_company(self, company):
        """
        Actualizar una empresa en la base de datos

        :param company: detalles de la empresa como una tupla
        :return: id de la empresa
        """
        sql = ''' UPDATE companies SET name = ?, description = ? WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql, company)
        self.conn.commit()
        return cur.lastrowid


    # ================== DELETE =====================
    def delete_user(self, id):
        """
        Eliminar un usuario de la base de datos

        :param id: id del usuario
        :return: id
        """
        sql = 'DELETE FROM users WHERE id = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()
        return cur.lastrowid

    def delete_company(self, id):
        """
        Eliminar una empresa de la base de datos

        :param id: id de la empresa
        :return: id
        """
        sql = 'DELETE FROM companies WHERE id = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()
        return cur.lastrowid

    # ================== SELECT =====================
    def get_user(self, id):
        """
        Obtener un usuario de la base de datos por su id

        :param id: id del usuario
        :return: usuario como una tupla
        """
        sql = 'SELECT * FROM users WHERE id = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        row = cur.fetchone()
        return row

    def get_users(self):
        """
        Obtener todos los usuarios de la base de datos

        :return: usuarios como una lista de tuplas
        """
        sql = 'SELECT * FROM users'
        cur = self.conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows

    def get_company(self, id):
        """
        Obtener una empresa de la base de datos por su id

        :param id: id de la empresa
        :return: empresa como una tupla
        """
        sql = 'SELECT * FROM companies WHERE id = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        row = cur.fetchone()
        return row

    def get_companies(self):
        """
        Obtener todas las empresas de la base de datos
        
        :return: empresas como una lista de tuplas
        """
        sql = 'SELECT * FROM companies'
        cur = self.conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows

def serv_crear_tablas(crud:Crud):
    """
    Servicio para crear tablas en la base de datos con las siguientes consultas SQL

    :param crud: objeto de la clase Crud
    """
    sql_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                id integer PRIMARY KEY,
                                username text NOT NULL,
                                email text,
                                age text,
                                password text
                            ); """
    sql_companies_table = """ CREATE TABLE IF NOT EXISTS companies (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                description text
                            ); """ 
    if crud.conn is not None:
        # Llama a la método create_table() de la clase Crud
        crud.create_table(sql_users_table)
        crud.create_table(sql_companies_table)
    else:
        print("Error! Cannot create the database connection.")

def serv_insertar_datos(crud:Crud):
    """
    Servicio para iknsertar datos en la base de datos

    :param crud: objeto de la clase Crud
    :return: lista de listas con los ids de los datos insertados
    """
    usuarios = [
        ('admin', 'admin@email.com', '32', 'admin'),
        ('user1', 'user1@email.com', '31', 'user1'),
        ('Victor', 'victor@email.com', '23', 'password')
    ]
    empresas = [
        ('Google', 'Esta es la descripción de Google'),
        ('Microsoft', 'Esta es la descripción de Microsoft')
    ]
    id_usuarios = []
    id_empresas = []
    if crud.conn is not None:
        # Llama a la método insert_user() de la clase Crud
        for user in usuarios:
            id_usuarios.append(crud.insert_user(user))
        # llama a la método insert_company() de la clase Crud
        for company in empresas:
            id_empresas.append(crud.insert_company(company))
    else:
        print("Error! Cannot create the database connection.")

    print(f"IDs Usuarios creados: " + ', '.join(str(id) for id in id_usuarios))
    print(f"IDs Empresas creadas: " + ', '.join(str(id) for id in id_empresas))
    return id_usuarios, id_empresas

def serv_actualizar_datos(crud:Crud):
    user_2 = ('user2', 'user2@email.com', '22', 'user2', 2)
    company_1 = ('Google_2', '¡Google es la mejor!', 1)
    
    if crud.conn is not None:
        with crud.conn:
            # Llama a la método update_user() de la clase Crud
            crud.update_user(user_2)
            # Llama a la método update_company() de la clase Crud
            crud.update_company(company_1)
    else:
        print("Error! Cannot create the database connection.")

    print(f"Usuario actualizado: {user_2}")
    print(f"Empresa actualizada: {company_1}")
    
def serv_obtener_datos(crud:Crud, by_id: bool=False):
    """
    Servicio para obtener datos de la base de datos
    
    :param crud: objeto de la clase Crud
    :param by_id: si se quiere obtener por id
    """
    id_user = 3
    id_company = 2
    if crud.conn is not None:
        with crud.conn:
            # Si está habilitado el parámetro by_id se obtienen los datos por id de usuario y empresa si no, se obtienen todos
            if by_id:
                # Llama a la método get_user() y get_company() de la clase Crud
                user = crud.get_user(id_user)
                company = crud.get_company(id_company)
                # Imprime los datos de usuario y empresa
                print(user)
                print(company)
            else:
                # Llama a la método get_users() y get_companies() de la clase Crud
                users = crud.get_users()
                companies = crud.get_companies()
                # Imprime los datos de todos los usuarios y empresas
                print(users)
                print(companies)
    else:
        print("Error! Cannot create the database connection.")

def serv_eliminar_datos(crud:Crud):
    """
    Servicio para eliminar datos de la base de datos
    
    :param crud: objeto de la clase Crud
    """
    id_user = 3
    id_company = 2
    if crud.conn is not None:
        with crud.conn:
            # Llama a la método delete_user() y delete_company() de la clase Crud para eliminar los datos por id
            crud.delete_user(id_user)
            crud.delete_company(id_company)
    else:
        print("Error! Cannot create the database connection.")

def main():
    """
    Función principal que invoca a los servicios para crear, insertar, actualizar, obtener y eliminar datos de la base de datos
    Descomentar para realizar las acciones (en caso de que estén comentadas)
    """
    # Crea una instancia de la clase Crud
    crud = Crud(DB_FILE)

    # ================== CREATE =====================   
    # Llama al servicio para crear tablas
    serv_crear_tablas(crud)
    # ================== INSERT =====================
    # Llama al servicio para insertar datos
    serv_insertar_datos(crud)
    # ================== UPDATE =====================
    # Llama al servicio para actualizar datos
    serv_actualizar_datos(crud)
    # ================== SELECT =====================
    # Llama al servicio para obtener todos datos 
    print("\nObtener todos los registros")
    serv_obtener_datos(crud, by_id=False)
    print("\nObtener registro por ID")
    # Llama al servicio para obtener datos por id
    serv_obtener_datos(crud, by_id=True)
    print("")
    # ================== DELETE =====================
    # Llama al servicio para eliminar datos por id
    serv_eliminar_datos(crud)

if __name__ == '__main__':
    main()