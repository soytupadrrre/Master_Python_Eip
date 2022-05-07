"""
Flask API REST

Script creado para la asignatura de Creación de aplicaciones Python de la Escuela Internacional de Postgrados.
Visualizar contenido dentro del Readme para más información.

Lanzamiento de la aplicación Flask: 
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
from flask import Flask, redirect
from flaskr.router.iris_router import iris_router

app = Flask(__name__)

# ==========================
#       IRIS REST API
# ==========================

# Redireccionamiento a la página de iris
@app.route('/', methods=["GET"])
def index():
    """
    Main page of the API

    :return: Redirect to iris/
    """
    return redirect('api/iris')

# Carga de aplicación iris
app.register_blueprint(iris_router, url_prefix="/api/iris")

# ==========================
#    END IRIS REST API
# ==========================     

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")