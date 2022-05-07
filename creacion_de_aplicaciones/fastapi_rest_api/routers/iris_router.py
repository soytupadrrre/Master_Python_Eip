from fastapi import APIRouter
from controllers.rest_iris import RestIris
from models.iris import Iris, IrisDelete

# Creación del objeto RestIris
rest_iris = RestIris("data/iris.csv")

# Creación de Router para la aplicación iris (mayor escalabilidad)
iris_router = APIRouter()

# Metodo GET para la página principal de iris
@iris_router.get("", status_code=200)
async def get_iris_data():
    payload = rest_iris.get_data()
    return payload

# Metodo GET para la página resumen de iris
@iris_router.get("/describe", status_code=200)
async def get_iris_resume():
    payload = rest_iris.get_resume()
    return payload

# Metodo GET para la página de precisión algoritmos ML implementados en iris
@iris_router.get("/accuracy", status_code=200)
async def get_iris_accuracy():
    payload = rest_iris.get_accuracy()
    return payload

# Metodo POST para insertar una nueva fila en iris
@iris_router.post("/insert", status_code=201)
async def post_iris_data(iris:Iris):
    data = iris.dict()
    inserted_data = rest_iris.post_data(data)
    payload = {
        "message": "Data inserted",
        "data": inserted_data
    }
    return payload

# Metodo POST para insertar y predecir una nueva fila en iris
@iris_router.post("/predict", status_code=201)
async def post_iris_predict(iris: Iris):
    data = iris.dict()
    predicted_data = rest_iris.post_predict(data)
    payload =  {
        "message": "Prediction done",
        "data": predicted_data
    }
    return payload

# Metodo PUT para actualizar el último registro de iris
@iris_router.put("/update-last", status_code=201)
async def put_iris_last_row(iris:Iris):
    data = iris.dict()
    updated_data = rest_iris.put_last_row(data)
    payload =  {
        "message": "Data updated",
        "data": updated_data
    }
    return payload

# Metodo PUT para actualizar una fila en iris dado un ID
@iris_router.put("/update", status_code=201)
async def put_iris_by_id(iris: Iris):
    data = iris.dict()
    updated_data = rest_iris.put_by_id(data)
    payload = {
        "message": "Data updated",
        "data": updated_data
    }
    return payload

# Metodo DELETE para eliminar la última fila de iris
@iris_router.delete("/delete-last", status_code=200)
async def delete_iris_last_row():
    rest_iris.delete_last_row()
    payload = {
        "message": "Data deleted"
    }
    return payload

# Metodo DELETE para eliminar una fila de iris dado un ID
@iris_router.delete("/delete", status_code=200)
async def delete_iris_by_id(iris: IrisDelete):
    data = iris.dict()
    deleted_id = rest_iris.delete_by_id(data)
    payload = {
        "message": "Data deleted",
        "id": deleted_id
    }
    return payload