from pywebio import input
from pywebio import output
from rest_iris import RestIris
from pywebio import config
from app import helper

def eliminar(data):
    RestIris().delete_by_id(data)
    output.put_success(f"Se han eliminado los datos en el Iris Dataset con id {data['id']}")

@config(title="Eliminar datos", description="Eliminar datos")
def app_eliminar():
    """
    Eliminar datos a través de formulario
    """
    helper.menu()
    # Seccion eliminar
    output.span(output.put_markdown("## Sección Eliminar"))
    output.put_markdown(f"Eliminar una fila")
    form_delete = input.input_group("Eliminar Datos", [
        input.input(label="ID", type=input.NUMBER, name="id"),
    ])
    eliminar(form_delete)