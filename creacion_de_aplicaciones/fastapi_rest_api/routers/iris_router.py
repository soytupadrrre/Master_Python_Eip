from fastapi import APIRouter
from ..controllers.rest_iris import RestIris
from ..models.iris import Iris, IrisDelete
from pathlib import Path

# Creación del objeto RestIris
rest_iris = RestIris("data/iris.csv")
"""
Creación del objeto :class:`fastapi_rest_api.controllers.rest_iris.RestIris`
"""

# Creación de Router para la aplicación iris (mayor escalabilidad)
iris_router = APIRouter()
"""
Generación de APIRouter
"""

# Metodo GET para la página principal de iris
@iris_router.get("", status_code=200)
async def get_iris_data() -> dict:
    """
    Punto de entrada principal de /api/iris
    Muestra los datos de Iris Dataset

    :return: Diccionario con la respuesta
    :rtype: dict
    """
    payload = rest_iris.get_data()
    return payload

# Metodo GET para la página resumen de iris
@iris_router.get("/describe", status_code=200)
async def get_iris_resume() -> dict:
    """
    Metodo GET para obtener un resumen de los datos desde /api/iris/endpoint

    :return: Diccionario con la respuesta
    :rtype: dict
    """
    payload = rest_iris.get_resume()
    return payload

# Metodo GET para la página de precisión algoritmos ML implementados en iris
@iris_router.get("/accuracy", status_code=200)
async def get_iris_accuracy() -> dict:
    """
    Metodo GET para obtener la precisión de los algoritmos implementados
    desde /api/iris/accuracy

    :return: Diccionario con la respuesta
    :rtype: dict
    """
    payload = rest_iris.get_accuracy()
    return payload

# Metodo POST para insertar una nueva fila en iris
@iris_router.post("/insert", status_code=201)
async def post_iris_data(iris:Iris) -> dict:
    """
    Método POST para insertar nuevos datos en iris dataset desde /api/iris/insert

    :param iris: Objeto Iris entrante
    :type iris: Iris
    :return: Diccionario con la respuesta
    :rtype: dict
    """
    data = iris.dict()
    inserted_data = rest_iris.post_data(data)
    payload = {
        "message": "Data inserted",
        "data": inserted_data
    }
    return payload

# Metodo POST para insertar y predecir una nueva fila en iris
@iris_router.post("/predict", status_code=201)
async def post_iris_predict(iris: Iris) -> dict:
    """
    
    Método POST para predecir una nueva especie en base a los datos introducidos desde /api/iris/predict

    :param iris: Objeto Iris entrante
    :type iris: Iris
    :return: Diccionario con la respuesta
    :rtype: dict
    """
    data = iris.dict()
    predicted_data = rest_iris.post_predict(data)
    payload =  {
        "message": "Prediction done",
        "data": predicted_data
    }
    return payload

# Metodo PUT para actualizar el último registro de iris
@iris_router.put("/update-last", status_code=201)
async def put_iris_last_row(iris:Iris) -> dict:
    """
    Método PUT para actualizar la última fila de Iris dataset desde /api/iris/update-last

    :param iris: Objeto Iris a actualizar
    :type iris: Iris
    :return: Diccionario con la respuesta
    :rtype: dict
    """
    data = iris.dict()
    updated_data = rest_iris.put_last_row(data)
    payload =  {
        "message": "Data updated",
        "data": updated_data
    }
    return payload

# Metodo PUT para actualizar una fila en iris dado un ID
@iris_router.put("/update", status_code=201)
async def put_iris_by_id(iris: Iris) -> dict:
    """
    Método PUT para actualizar un registro de Iris dataset basado en un ID desde /api/iris/update

    :param iris: Objeto Iris a actualizar
    :type iris: Iris
    :return: Diccionario con la respuesta
    :rtype: dict
    """
    data = iris.dict()
    updated_data = rest_iris.put_by_id(data)
    payload = {
        "message": "Data updated",
        "data": updated_data
    }
    return payload

# Metodo DELETE para eliminar la última fila de iris
@iris_router.delete("/delete-last", status_code=200)
async def delete_iris_last_row() -> dict:
    """
    Método DELETE para eliminar el ultimo registro de Iris Dataset desde /api/iris/update-last

    :return: Diccionario con la respuesta
    :rtype: dict
    """
    rest_iris.delete_last_row()
    payload = {
        "message": "Data deleted"
    }
    return payload

# Metodo DELETE para eliminar una fila de iris dado un ID
@iris_router.delete("/delete", status_code=200)
async def delete_iris_by_id(iris: IrisDelete) -> dict:
    """
    Método DELETE para eliminar un registro de Iris dataset a partir de un ID desde /api/iris/delete

    :param iris: Objeto Iris a Eliminar
    :type iris: IrisDelete
    :return: Diccionario con la respuesta
    :rtype: dict
    """
    data = iris.dict()
    deleted_id = rest_iris.delete_by_id(data)
    payload = {
        "message": "Data deleted",
        "id": deleted_id
    }
    return payload