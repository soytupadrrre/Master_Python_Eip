from pywebio import input
from pywebio import output
from rest_iris import RestIris
from pywebio import config
from app import helper

def predecir(data):
    data = RestIris().post_predict(data)
    msg = [
        f"Se ha utilizado el clasificador: {data['predicted_model']}",
        f"La especie predicha por el clasificador es: {data['predicted_species']}",
        f"Se ha añadido los datos en el Iris Dataset con id {data['id']}"
    ]
    output.put_success("\n".join(msg))


@config(title="Predecir Datos", description="Predecir especie de iris")
def app_prediccion():
    """
    Predecir especie de iris
    """
    helper.menu()
    # Seccion Machine Learning (Predicción)
    output.put_markdown("## Sección Machine Learning (Predicción)")
    output.put_markdown(f"Predicción de una nueva fila")
    form_ml = input.input_group("Predecir Datos", [
        input.input(label="Sepal Length (cm)", type=input.FLOAT, name="sepal_length"),
        input.input(label="Sepal Width (cm)", type=input.FLOAT, name="sepal_width"),
        input.input(label="Petal Length (cm)", type=input.FLOAT, name="petal_length"),
        input.input(label="Petal Width (cm)", type=input.FLOAT, name="petal_width"),
        input.select(label="Classifier:", options=["DecissionTree", "RandomTree"], name="classifier"),
    ])
    predecir(form_ml)