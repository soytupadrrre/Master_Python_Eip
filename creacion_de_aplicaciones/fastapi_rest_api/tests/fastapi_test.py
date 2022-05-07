import pytest
import requests

# Fichero para realizar test de la API creada en Flask

base_url = "http://localhost:8000/api/"

# Comprueba que la página de inicio de la API es la correcta
def test_get_iris_data():
    response = requests.get(base_url + "iris")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Comprueba que la página de descripción de la API es la correcta
def test_get_iris_resume():
    response = requests.get(base_url + "iris/describe")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "count" in response.json()
    assert "mean" in response.json()
    assert "std" in response.json()
    assert "min" in response.json()
    assert "max" in response.json()
    assert "25%" in response.json()
    assert "50%" in response.json()
    assert "75%" in response.json()

# Comprueba que la página de precisión de la API es la correcta
def test_get_iris_accuracy():
    response = requests.get(base_url + "iris/accuracy")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "species" in response.json()
    assert "setosa" in response.json()["species"]
    assert "versicolor" in response.json()["species"]
    assert "virginica" in response.json()["species"]
    assert "algorithms" in response.json()
    assert len(response.json()["algorithms"]) == 2
    for algorithm in response.json()["algorithms"]:
        assert "name" in algorithm
        assert "results" in algorithm
        assert "accuracy" in algorithm["results"]
        assert "predicted" in algorithm["results"]
        assert isinstance(algorithm["results"]["predicted"], list)
        assert "real" in algorithm["results"]
        assert isinstance(algorithm["results"]["real"], list)

# Comprueba que la página de inserción de la API es la correcta
def test_post_iris_data():
    data = {
        "petal_length": 100, 
        "petal_width": 100, 
        "sepal_length": 100, 
        "sepal_width": 100, 
        "species": "setosa"
    }
    response = requests.post(base_url + "iris/insert", json=data)
    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert "message" in response.json()
    assert response.json()["message"] == "Data inserted"
    assert "data" in response.json()
    assert isinstance(response.json()["data"], dict)
    assert "id" in response.json()["data"]
    assert "petal_length" in response.json()["data"]
    assert "petal_width" in response.json()["data"]
    assert "sepal_length" in response.json()["data"]
    assert "sepal_width" in response.json()["data"]
    assert "species" in response.json()["data"]

# Comprueba que la página de predicción de la API es la correcta
@pytest.mark.parametrize("data, expected", [
    ({
        "petal_length": 50,
        "petal_width": 50,
        "sepal_length": 50,
        "sepal_width": 50,
        "classifier": "DecissionTree"
        }, "virginica")]
)
def test_post_iris_predict(data, expected):
    response = requests.post(base_url + "iris/predict", json=data)
    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert "message" in response.json()
    assert response.json()["message"] == "Prediction done"
    assert "data" in response.json()
    assert isinstance(response.json()["data"], dict)
    assert "predicted_species" in response.json()["data"]
    assert response.json()["data"]["predicted_species"] == expected
    assert "id" in response.json()["data"]
    assert "petal_length" in response.json()["data"]
    assert "petal_width" in response.json()["data"]
    assert "sepal_length" in response.json()["data"]
    assert "sepal_width" in response.json()["data"]
    assert "classifier" in response.json()["data"]
    assert "predicted_model" in response.json()["data"]

# Comprueba que la página de actualización de la API es la correcta
@pytest.mark.parametrize("data, expected", [(
        {
            "petal_length": 4,
            "petal_width": 4,
            "sepal_length": 4,
            "sepal_width": 4,
            "species": "teest"
        }, {
            "data": {
                "id": 199,
                "petal_length": 4,
                "petal_width": 4,
                "sepal_length": 4,
                "sepal_width": 4,
                "species": "teest"
            },
            "message": "Data updated"
        }
    ),(
        {
            "petal_length": 300,
            "petal_width": 300,
            "sepal_length": 300,
            "sepal_width": 300,
            "species": "azul"
        }, {
        "data": {
            "petal_length": 300,
            "petal_width": 300,
            "sepal_length": 300,
            "sepal_width": 300,
            "species": "azul"
        },
        "message": "Data updated"
        }
    )]
)
def test_post_iris_update_last(data, expected):
    response = requests.put(base_url + "iris/update-last", json=data)
    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert "message" in response.json()
    assert response.json()["message"] == expected["message"]
    assert "data" in response.json()
    assert isinstance(response.json()["data"], dict)
    assert response.json()["data"]["petal_length"] == expected["data"]["petal_length"]
    assert response.json()["data"]["petal_width"] == expected["data"]["petal_width"]
    assert response.json()["data"]["sepal_length"] == expected["data"]["sepal_length"]
    assert response.json()["data"]["sepal_width"] == expected["data"]["sepal_width"]
    assert response.json()["data"]["species"] == expected["data"]["species"]

# Comprueba que la página de actualización de la API es la correcta
@pytest.mark.parametrize("data, expected", [(
        {
            "id": 193,
            "petal_length": 50, 
            "petal_width": 50, 
            "sepal_length": 50, 
            "sepal_width": 50, 
            "species": "edicionporid1"
        },{
            "message": "Data updated",
            "data": {
                "petal_length": 50,
                "petal_width": 50,
                "sepal_length": 50,
                "sepal_width": 50,
                "species": "edicionporid1"
            }
        }),(
            {
            "id": 193,
            "petal_length": 1, 
            "petal_width": 1, 
            "sepal_length": 1, 
            "sepal_width": 1, 
            "species": "edicionporid2"
        },{
            "message": "Data updated",
            "data": {
                "petal_length": 1,
                "petal_width": 1,
                "sepal_length": 1,
                "sepal_width": 1,
                "species": "edicionporid2"
            }
        })])
def test_post_iris_update(data, expected):
    response = requests.put(base_url + "iris/update", json=data)
    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert "message" in response.json()
    assert response.json()["message"] == expected["message"]
    assert "data" in response.json()
    assert isinstance(response.json()["data"], dict)
    assert response.json()["data"]["petal_length"] == expected["data"]["petal_length"]
    assert response.json()["data"]["petal_width"] == expected["data"]["petal_width"]
    assert response.json()["data"]["sepal_length"] == expected["data"]["sepal_length"]
    assert response.json()["data"]["sepal_width"] == expected["data"]["sepal_width"]
    assert response.json()["data"]["species"] == expected["data"]["species"]

# Comprueba que la página de eliminación de la API es la correcta
@pytest.mark.parametrize("data, expected", [(
        {
            "id": 193
        },{
            "message": "Data deleted",
            "id": 193
        })])
def test_post_iris_delete(data, expected):
    response = requests.delete(base_url + "iris/delete", json=data)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "message" in response.json()
    assert response.json()["message"] == expected["message"]
    assert "id" in response.json()
    assert response.json()["id"] == expected["id"]

# Comprueba que la página de eliminación de la API es la correcta
def test_post_iris_delete_last():
    response = requests.delete(base_url + "iris/delete-last")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "message" in response.json()
    assert response.json()["message"] == "Data deleted"
