# Flask API REST
Script creado para la asignatura de Creación de aplicaciones Python de la Escuela Internacional de Postgrados, lección 8.

## Autor
* Nombre: Víctor Luque Martín<br>
* Fecha: 07-05-2022<br>
* Versión: 1.0<br>
* Email: [victorluque341@gmail.com](mailto:victorluque341@gmail.com)

## Comprobación funcionamiento de la aplicación:
1. Lanzar aplicación Flask
2. Ejecutar los tests dentro del fichero test/flask_api_test.py

## Lanzamiento de la aplicación Flask: 
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

## Rutas de la aplicación:

### MÉTODO GET

#### Ruta: /api/iris/
Muestra todos los datos de Iris Dataset.

#### Ruta: /api/iris/describe
Devuelve un resumen de los datos contenidos en Iris.csv

#### Ruta: /api/iris/accuracy
Devuelve los datos de precision de los modelos de predicción implementados en la aplicación ademas de los datos de cada especie:
- Decission Tree Classifier 
- Random Forest Classifier

### MÉTODO POST
#### Ruta: /api/iris/insert
Inserta una nueva fila en la tabla iris.
- Parámetros:
    - petal_length (float): Longitud del pétalo.
    - petal_width (float): Ancho del pétalo.
    - sepal_length (float): Longitud del sépalo.
    - sepal_width (float): Ancho del sépalo.
    - species (string): Especie de la planta. 
```json
{
    "petal_length": 3.2, 
    "petal_width": 0.2, 
    "sepal_length": 5.2, 
    "sepal_width": 4.3, 
    "species": "setosa"
}
```

### Ruta: /api/iris/predict
Predice la especie de una planta.
- Parámetros:
    - petal_length (float): Longitud del pétalo.
    - petal_width (float): Ancho del pétalo.
    - sepal_length (float): Longitud del sépalo.
    - sepal_width (float): Ancho del sépalo.
    - predict_model (string): Modelo a utilizar para la predicción (DecissionTree o RandomForest).
```json
{
    "petal_length": 3.2, 
    "petal_width": 0.2, 
    "sepal_length": 5.2, 
    "sepal_width": 4.3, 
    "classifier": "DecissionTree"
}
```
### MÉTODO PUT
#### Ruta: /api/iris/update-last
Actualiza la última fila de la tabla iris.
```json
{
    "sepal_length": 5.4, 
    "sepal_width": 4.5, 
    "petal_length": 3.2, 
    "petal_width": 0.2, 
    "species": "versicolor"
}
```

#### Ruta: /api/iris/update
Actualiza una fila de la tabla iris dado un id.
```json
{
    "id": 193, 
    "sepal_length": 1.1, 
    "sepal_width": 1.1, 
    "petal_length": 1.1, 
    "petal_width": 1.1, 
    "species": "virginica"
}
```
### MÉTODO DELETE
#### Ruta: /api/iris/delete-last
Elimina la última fila de la tabla iris.

#### Ruta: /api/iris/delete
Elimina una fila de la tabla iris dado un id.
```json
{
    "id": 193
}
```