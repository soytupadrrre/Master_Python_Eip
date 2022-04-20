"""
Flask API REST

Script creado para la asignatura de Creación de aplicaciones Python de la Escuela Internacional de Postgrados

Uso: 
- Windows:
    - Powershell:
        - $env:FLASK_APP = "flaskr"
        - $env:FLASK_ENV = "development"
        - flask run
    - CMD:
        - set FLASK_APP=flaskr
        - set FLASK_ENV=development
        - flask run
- Linux & MacOS:
    - export FLASK_APP=flaskr
    - export FLASK_ENV=development
    - flask run

@autor: Víctor Luque Martín
@fecha: 20-04-2022
@versión: 1.0
@licencia: MIT
@email: victorluque341@gmail.com
"""
from flask import Flask, request, redirect
from .controller import get_methods, post_methods, put_methods, delete_methods

# Methods available for the API
# GET - Retrieve resume data
# POST - Create a new record
# PUT - Update an existing record (by ID or last row)
# DELETE - Delete a record (by ID or last row)

"""
USE Examples as payloads for the requests
/iris/insert-data = {
    "petal_length": 3.2, 
    "petal_width": 0.2, 
    "sepal_length": 5.2, 
    "sepal_width": 4.3, 
    "species": "setosa"
}

/iris/update-last-row = {
    "sepal_length": 5.4, 
    "sepal_width": 4.5, 
    "petal_length": 3.2, 
    "petal_width": 0.2, 
    "species": "versicolor"
}

/iris/update-by-id = {
    "id": 193, 
    "sepal_length": 1.1, 
    "sepal_width": 1.1, 
    "petal_length": 1.1, 
    "petal_width": 1.1, 
    "species": "virginica"
}

/iris/delete-by-id = {
    "id": 193
}
"""

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    """
    Main page of the API

    :return: Redirect to iris/
    """
    return redirect('iris')

# ==========================
#       IRIS REST API
# ==========================

# SHOW IRIS RESUME - GET
@app.route("/iris/", methods=["GET"])
def iris_data():
    """
    Show the resume of the iris data

    :return: JSON with the resume of the iris data
    """
    return get_methods.get_iris_resume()

# INSERT DATA INTO IRIS - POST
@app.route("/iris/insert-data/", methods=["POST"])
def insert_data():
    """
    Insert a new record into the iris data

    :return: JSON with the new record inserted
    """
    return post_methods.insert_iris_data(request.data)

# UPDATE IRIS BY ID - PUT
@app.route("/iris/update-by-id/", methods=["PUT"])
def update_by_id():
    """
    Update an existing record in the iris data by id

    :return: JSON with the record updated
    """
    return put_methods.update_iris_by_id(request.data)

# UPDATE IRIS LAST ROW - PUT
@app.route("/iris/update-last-row/", methods=["PUT"])
def update_last_row():
    """
    Update the last record in the iris data
    
    :return: JSON with the record updated
    """    
    return put_methods.update_iris_last_row(request.data)

# DELETE IRIS LAST ROW - DELETE
@app.route("/iris/delete-last/", methods=["DELETE"])
def delete_last():
    """
    Delete the last record in the iris data
    
    :return: JSON with the record deleted
    """
    return delete_methods.delete_iris_last_row()

# DELETE IRIS BY ID - DELETE
@app.route("/iris/delete-by-id/", methods=["DELETE"])
def delete_by_id():
    """
    Delete an existing record in the iris data by id
    
    :return: JSON with the record deleted
    """
    return delete_methods.delete_iris_by_id(request.data)

# ==========================
#    END IRIS REST API
# ==========================     

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")