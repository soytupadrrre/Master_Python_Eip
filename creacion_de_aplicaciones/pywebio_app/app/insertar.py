from pywebio import input
from pywebio import output
from rest_iris import RestIris
from pywebio import config
from app import helper

def insertar(data):
    data = RestIris().post_data(data)
    output.put_success(f"Se ha añadido los datos en el Iris Dataset con id {data['id']}")

@config(title="Insertar Datos", description="Insertar nuevos datos")
def app_insertar():
    """
    Insertar datos a través de formulario
    """
    helper.menu()
    # Seccion insertar
    output.put_markdown("## Sección Insertar")
    output.put_markdown(f"Insertar una nueva fila")
    form_insert = input.input_group("Insertar Datos", [
        input.input(label="Sepal Length (cm)", type=input.FLOAT, name="sepal_length"),
        input.input(label="Sepal Width (cm)", type=input.FLOAT, name="sepal_width"),
        input.input(label="Petal Length (cm)", type=input.FLOAT, name="petal_length"),
        input.input(label="Petal Width (cm)", type=input.FLOAT, name="petal_width"),
        input.select(label="Species:", options=["setosa", "virginica", "versicolor"], name="species"),
    ])
    insertar(form_insert)