# Flask API REST
Script creado para la asignatura de Creación de aplicaciones Python de la Escuela Internacional de Postgrados, lección 8.

## Autor
* nombre: Víctor Luque Martín<br>
* fecha: 07-05-2022<br>
* versión: 1.0<br>
* email: [victorluque341@gmail.com](mailto:victorluque341@gmail.com)

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
#### Ruta: /iris/
Devuelve un resumen de los datos contenidos en Iris.csv

#### Ruta: /iris/accuracy
Devuelve los datos de precision de los modelos de predicción implementados en la aplicación ademas de los datos de cada especie:
- Decission Tree Classifier 
- Random Forest Classifier

### MÉTODO POST
#### Ruta: /iris/insert-data
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

### Ruta: /iris/predict
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
#### Ruta: /iris/update-last-row
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

#### Ruta: /iris/update-by-id
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
#### Ruta: /iris/delete-last
Elimina la última fila de la tabla iris.

#### Ruta: /iris/delete-by-id
Elimina una fila de la tabla iris dado un id.
```json
{
    "id": 193
}
```
