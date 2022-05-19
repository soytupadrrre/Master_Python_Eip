import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/iris.csv")

app = dash.Dash(title="Víctor Luque - Iris Dash App")

@app.callback(
    Output(component_id='output', component_property='figure'),
    [Input(component_id='input', component_property='value')]
)
def create_figure(input: str="Todas"):
    # filter df
    input = input.lower() 
    if input == 'todas':
        df_filtered = df
    else:
        df_filtered = df[df['species'] == input]
    figure = px.scatter(
        df_filtered, x="sepal_length", y="sepal_width", 
        color="species", size="sepal_length", 
        title="Iris Sepal", labels={"sepal_length": "Largo del Sépalo (cm)", "sepal_width": "Ancho del Sépalo (cm)", "species": "Especies de Iris"}
    )
    return figure

lista = [["Todas", "Todas"], ["Setosa", "Setosa"], ["Versicolor", "Versicolor"], ["Virginica", "Virginica"]]
app.layout = html.Div(children=[
    html.H1(children='Víctor Luque - Dash App'),
    html.H3(children='''
        Una aplicación de Dash para mostrar la información del sépalo de las flores iris contenidas en Iris Dataset.
    '''),
    html.P("Seleccione una especie para ver su sépalo (setosa, version, virginica, todas)"),
    dcc.Dropdown(
        id='input',
        options=[
            {'label': i[0], 'value': i[1]} for i in lista
        ],
        value='Todas'
    ),
    # Create a figure
    dcc.Graph(id='output'),
])


if __name__ == '__main__':
    app.run_server(debug=True)
