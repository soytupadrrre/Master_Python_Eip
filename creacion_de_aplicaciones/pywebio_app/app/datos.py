from pywebio import output
from rest_iris import RestIris
import plotly.express as px
import plotly.graph_objects as go
from pywebio import config
from app import helper

def ver_datos_sepalo():
    df = RestIris().get_data()    

    fig = px.scatter(
        df, x="sepal_length", y="sepal_width", 
        color="species", title="Iris Dataset Sepal Plot", 
        labels={
            "sepal_length": "Sepal Length", 
            "sepal_width": "Sepal Width", 
            "species": "Species"
        }
    )
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    return html

def ver_datos_petalo():
    df = RestIris().get_data()
    fig = px.scatter(
        df, x="petal_length", y="petal_width", 
        color="species", title="Iris Dataset Petal Plot", 
        labels={
            "petal_length": "Petal Length", 
            "petal_width": "Petal Width", 
            "species": "Species"
        }
    )
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    return html

def ver_resumen():
    summary = RestIris().get_summary()
    # Remove id column
    summary.drop(columns=["id"], inplace=True)
    # delete row count
    
    summary.rename(columns={
        "sepal_length": "Sepal Length (cm)", 
        "sepal_width": "Sepal Width (cm)", 
        "petal_length": "Petal Length (cm)", 
        "petal_width": "Petal Width (cm)", 
        "species": "Species"
    }, inplace=True)
    # invert columns and rows
    summary = summary.transpose()
    cols = summary.columns
    # create fig from dataframe
    fig = go.Figure(go.Bar(x=summary.index, y=summary[cols[0]].values.tolist(), name=cols[0], text=summary[cols[0]].values.tolist(), textposition="auto"))
    for col in cols[1:]:
        fig.add_trace(go.Bar(x=summary.index, y=summary[col].values.tolist(), name=col, text=summary[col].values.tolist(), textposition="auto"))
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'})
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    return html

@config(title="Mostrar Datos", description="Muestra los datos del Iris Dataset gráficamente")
def app_datos():
    """
    Aplicacion para mostrar datos relacionados con Iris Dataset

    Se incluyen un gráfico de barras para el resumen del dataset y dos gráficos de dispersión para los datos de Sepal y Petal
    """
    helper.menu()

    # Seccion Datos
    output.put_grid([
        [output.span(output.put_markdown("## Sección Datos"), col=1)],
        [output.put_markdown("### Resumen")],
        [output.put_html(ver_resumen())],
        [output.put_grid([
            [output.span(output.put_markdown("### Datos"), col=2)],
            [output.put_markdown("Sepal"), output.put_markdown("Petal")],
            [output.put_html(ver_datos_sepalo()), output.put_html(ver_datos_petalo())],
        ])]
    ])