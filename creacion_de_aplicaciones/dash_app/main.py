from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import quandl
import requests
from io import StringIO
from configparser import ConfigParser
from dash import Dash

# Inicializar Dash
app = Dash(title="Víctor Luque - Quandl Dash App")
# Obtención de fuentes de datos a usar en Quandl
wiki_prices = "https://static.quandl.com/coverage/WIKI_PRICES.csv"
secwiki_tickers = "https://raw.githubusercontent.com/BangaloreSharks/SharkStock/master/secwiki_tickers.csv"
# Configurar Quandl
try:
    config = ConfigParser()
    config.read('config.ini')
    if not config.has_section('quandl'):
        raise Exception('No se encuentra la sección [quandl] en el archivo config.ini')
    quandl.ApiConfig.api_key = config['quandl']['api_key']
except Exception as e:
    print(e)
    print("No se usará la API KEY de Quandl")
    quandl.ApiConfig.api_key = ""

# Obtención de códigos WIKI/EMPRESA de Quandl
wiki_companies_text = requests.get(wiki_prices).text
wiki_companies_df = pd.read_csv(StringIO(wiki_companies_text))
wiki_companies_df.rename(columns={'ticker': 'Ticker'}, inplace=True)

# Obtención de datos sobre empresas de Quandl
data_secwiki = requests.get(secwiki_tickers).text
df_secwiki = pd.read_csv(StringIO(data_secwiki))
df_secwiki = df_secwiki[df_secwiki["Price"].notna()]

# Cruzar datos de tickers con datos de secwiki para
# crear DataFrame con tickers y empresas de Quandl
df_valid = pd.merge(wiki_companies_df, df_secwiki, on="Ticker")
df_valid = df_valid.drop(columns=["Industry", "Price", "Collection", "Sector"])
df_valid = df_valid[df_valid["Ticker"].notna()]
df_valid = df_valid[df_valid["Name"].notna()]

# Eliminar Dataframes innecesarios
del wiki_companies_df
del df_secwiki

# Obtener Dataframe de Quandl
def get_quandl_data(ticker, start_date, end_date):
    response = quandl.get(f"WIKI/{ticker}.4", start_date=start_date, end_date=end_date)
    # Agregar columna de ticker
    response["Ticker"] = ticker
    return response

# Crear figura de gráfico dinámicamente
@app.callback(
    Output(component_id='output', component_property='figure'),
    [Input(component_id='input_ticker', component_property='value'),
     Input(component_id='date_range', component_property='start_date'),
     Input(component_id='date_range', component_property='end_date')]
)
def create_figure(input_ticker:str, start_date:str, end_date:str):
    if input_ticker is not None:
        input_ticker = input_ticker.upper()
    else:
        input_ticker = 'GOOGL'
    # Collect data from Quandl
    # Create a figure
    df_quandl = get_quandl_data(input_ticker, start_date, end_date)
    # Move date index to a column
    df_quandl.reset_index(inplace=True)
    df_quandl.rename(columns={'Date': 'Date_Quandl'}, inplace=True)
    # Include rows from df_valid where ticker is the same as ticker from Quandl
    df_quandl = pd.merge(df_valid, df_quandl, on="Ticker")
    figure = px.line(
        df_quandl, x="Date_Quandl", y="Close",
        title="Precios de {}".format(df_valid[df_valid["Ticker"] == input_ticker]["Name"].to_string(index=False)),
        labels={
            "Close": "Precio de cierre (USD)",
            "Date_Quandl": "Fecha"
        },
        template="plotly_dark"
    )
    return figure

# Crear layout de la aplicación
app.layout = html.Div(children=[
    html.H1(children='Víctor Luque - Quandl Dash App'),
    html.H3(children='''
        Una aplicación de Dash para mostrar información del cierre en bolsa de empresas .
    '''),
    html.P("Seleccione una empresa para ver su cierre en bolsa"),
    dcc.Dropdown(
        id='input_ticker',
        options=[
            {'label': i[1], 'value': i[0]} for i in df_valid[["Ticker", "Name"]].values
        ],
        clearable=False,
        value='GOOG'
    ),
    dcc.DatePickerRange(
        id='date_range',
        min_date_allowed="2015-01-01",
        max_date_allowed="2021-12-31",
        start_date="2015-01-01",
        end_date="2021-12-31"

    ),
    dcc.Graph(id='output', figure=create_figure(input_ticker='GOOG', start_date='2015-01-01', end_date='2021-12-31')),
])

if __name__ == '__main__':
    app.run_server(debug=True)
