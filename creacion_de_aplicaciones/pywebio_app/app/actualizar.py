from pywebio import input
from pywebio import output
from rest_iris import RestIris
from pywebio import config
from app import helper

def actualizar(data):
    data = RestIris().put_by_id(data)
    output.put_success(f"Se han actualizado los datos en el Iris Dataset con id {data['id']}")

@config(title="Actualizar datos", description="Actualizar datos")
def app_actualizar():
    """
    Actualizar datos a través de formulario
    """
    helper.menu()
    # Seccion actualizar
    output.span(output.put_markdown("## Sección Actualizar"))
    output.put_markdown(f"Actualizar una fila")
    form_update = input.input_group("Actualizar Datos", [
        input.input(label="ID", type=input.NUMBER, name="id"),
        input.input(label="Sepal Length (cm)", type=input.FLOAT, name="sepal_length"),
        input.input(label="Sepal Width (cm)", type=input.FLOAT, name="sepal_width"),
        input.input(label="Petal Length (cm)", type=input.FLOAT, name="petal_length"),
        input.input(label="Petal Width (cm)", type=input.FLOAT, name="petal_width"),
        input.select(label="Species:", options=["setosa", "virginica", "versicolor"], name="species"),
    ])
    actualizar(form_update)
