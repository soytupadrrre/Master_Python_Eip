from flask import Blueprint, jsonify, request
from flaskr.controller.rest_iris import RestIris

# Creación del objeto RestIris
rest_iris = RestIris("data/iris.csv")

# Creación de Blueprint para la aplicación iris (mayor escalabilidad)
iris_router = Blueprint("iris_page", __name__)

# Metodo GET para la página principal de iris
@iris_router.route("/", methods=["GET"])
def get_iris_data():
    payload = rest_iris.get_data()
    return payload, 200

# Metodo GET para la página resumen de iris
@iris_router.route("/describe", methods=["GET"])
def get_iris_resume():
    payload = rest_iris.get_resume()
    return payload, 200

# Metodo GET para la página de precisión algoritmos ML implementados en iris
@iris_router.route("/accuracy", methods=["GET"])
def get_iris_accuracy():
    payload = rest_iris.get_accuracy()
    return jsonify(payload), 200

# Metodo POST para insertar una nueva fila en iris
@iris_router.route("/insert", methods=["POST"])
def post_iris_data():
    data = request.get_json()
    inserted_data = rest_iris.post_data(data)
    payload = {
        "message": "Data inserted",
        "data": inserted_data
    }
    return jsonify(payload), 201

# Metodo POST para insertar y predecir una nueva fila en iris
@iris_router.route("/predict", methods=["POST"])
def post_iris_predict():
    data = request.get_json()
    predicted_data = rest_iris.post_predict(data)
    payload =  {
        "message": "Prediction done",
        "data": predicted_data
    }
    return jsonify(payload), 201

# Metodo PUT para actualizar el último registro de iris
@iris_router.route("/update-last", methods=["PUT"])
def put_iris_last_row():
    data = request.get_json()
    updated_data = rest_iris.put_last_row(data)
    payload =  {
        "message": "Data updated",
        "data": updated_data
    }
    return jsonify(payload), 201

# Metodo PUT para actualizar una fila en iris dado un ID
@iris_router.route("/update", methods=["PUT"])
def put_iris_by_id():
    data = request.get_json()
    updated_data = rest_iris.put_by_id(data)
    payload = {
        "message": "Data updated",
        "data": updated_data
    }
    return jsonify(payload), 201

# Metodo DELETE para eliminar la última fila de iris
@iris_router.route("/delete-last", methods=["DELETE"])
def delete_iris_last_row():
    rest_iris.delete_last_row()
    payload = {
        "message": "Data deleted"
    }
    return jsonify(payload), 200

# Metodo DELETE para eliminar una fila de iris dado un ID
@iris_router.route("/delete", methods=["DELETE"])
def delete_iris_by_id():
    data = request.get_json()
    deleted_id = rest_iris.delete_by_id(data)
    payload = {
        "message": "Data deleted",
        "id": deleted_id
    }
    return jsonify(payload), 200