"""
Aplicacion de Finanzas para el control de errores

Script creado para la asignatura de Buenas Prácticas de Programación en Python de la Escuela Internacional de Postgrados.

Intalar las dependencias desde el fichero requirements.txt `pip install -r requirements.txt`

La aplicación es posible ejecutarla localmente empleando las librerías
- Pandas `pip install pandas`
- Matplotlib `pip install matplotlib`

En caso de utilizar la interfaz web de Streamlit, se debe instalar la librería de streamlit `pip install streamlit`
y ejecutar el programa con el comando `streamlit run app_finanzas.py`

@autor: Víctor Luque Martín
@fecha: 18-06-2022
@versión: 1.0
@licencia: MIT
@email: victorluque341@gmail.com
"""

import locale
from pathlib import Path

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError:
    print('No se puede importar pandas o matplotlib, por favor instalar ambos')
    exit()

# Descomentar lineas si se quiere ejecutar el programa con Streamlit
try:
    import streamlit as st
    import altair as alt
except ImportError:
    print('No se puede importar streamlit o altair, la aplicacion no puede ejecutarse desde la interfaz de streamlit')

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

def read_file(filepath: Path) -> str:
    """
    Función que lee el archivo csv y lo devuelve como un dataframe

    :param filepath: ruta del archivo csv
    :type filepath: Path
    :raises FileNotFoundError: Si el archivo no existe
    :return: dataframe con los datos del archivo
    :rtype: pd.DataFrame
    """
    try :
        # Lectura de fichero

        # Comprobación de que el archivo existe
        if not filepath.exists():
            raise FileNotFoundError('No se encuentra el archivo {}'.format(filepath))

        return pd.read_csv(filepath, sep='\t')

    except FileNotFoundError as e:
        raise e
        
def check_columns(df: pd.DataFrame) -> bool:
    """
    Función que comprueba que las columnas sean correctas

    :param df: dataframe con los datos del archivo
    :type df: pd.DataFrame
    :raises AssertionError: Si no se cumplen las condiciones
    :return: True si las columnas son correctas
    :rtype: bool
    """
    # Comprobación de que el fichero tiene 12 columnas
    assert len(df.columns) == 12, 'El fichero no tiene 12 columnas'
    # Comprobación de que los nombres de las columnas son correctos
    colnames = ['Enero', 'Febrero', 'Marzo', 
                'Abril', 'Mayo', 'Junio', 
                'Julio', 'Agosto', 'Septiembre', 
                'Octubre', 'Noviembre', 'Diciembre']
    assert df.columns.tolist() == colnames, 'Los nombres de las columnas no son correctos'
    return True

def parse_dataframe(df: pd.DataFrame):
    """
    Función que estandariza los datos del dataframe

    :param df: dataframe con los datos del archivo
    :type df: pd.DataFrame
    :raises ValueError: Si existen valores nulos
    :raises ValueError: Si existen valores no numéricos
    :return: dataframe con los datos estandarizados
    :rtype: pd.DataFrame
    """
    try: 
        for col in df.columns:
            # Comprobación de que no existen valores nulos
            if df[col].isnull().any():
                null_index = df.index[df[col].isnull()].tolist()
                raise ValueError('Hay un valor nulo en la columna {} en la fila: {}'.format(col, ','.join(null_index)))
            # Comprobación de que no existen valores no numéricos
            if df[col].dtype != 'float64' or df[col].dtype != 'int64':
                raise ValueError('Hay valores no numéricos en la columna {} serán reemplazados por 0'.format(col))

    except ValueError as e:
        print(e)

    finally:
        if df is not None:
            # Eliminación de valores no validos
            for col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            # Sustitución de valores no validos por 0
            df.fillna(0, inplace=True)
            return df

def most_spent_month(df: pd.DataFrame) -> list:
    """
    Función que devuelve el mes con mayor gasto y el importe total de ese mes

    :param df: dataframe con los datos del archivo
    :type df: pd.DataFrame
    :return: mes con mayor gasto y importe total de ese mes
    :rtype: list
    """
    df_gastos = df.copy()
    df_gastos.drop(columns=['Ahorros'], inplace=True)
    gastos = df_gastos.sum(axis=1)
    max_index = gastos.idxmax()
    max_value = gastos[max_index]
    return max_index, max_value

def most_saving_month(df: pd.DataFrame) -> list:
    """
    Función que devuelve el mes con menor gasto y el importe total de ese mes

    :param df: dataframe con los datos del archivo
    :type df: pd.DataFrame
    :return: mes con menor gasto y importe total de ese mes
    :rtype: list
    """
    df_ahorros = df.copy()
    df_ahorros.drop(columns=['Gastos'], inplace=True)
    ahorros = df_ahorros.sum(axis=1)
    min_index = ahorros.idxmax()
    min_value = ahorros[min_index]
    return min_index, min_value

def avg_spent(df: pd.DataFrame) -> float:
    """
    Función que devuelve el importe medio de gastos de todo el año

    :param df: dataframe con los datos del archivo
    :type df: pd.DataFrame
    :return: importe medio de gastos de todo el año
    :rtype: float
    """
    df_gastos = df.copy()
    df_gastos.drop(columns=['Ahorros'], inplace=True)
    gastos = df_gastos.sum(axis=1)
    return gastos.mean()

def total_spent_monthly(df: pd.DataFrame) -> float:
    """
    Función que devuelve el importe total de gastos a lo largo del año

    :param df: dataframe con los datos
    :type df: pd.DataFrame
    :return: importe total de gastos a lo largo del año
    :rtype: float
    """
    # Transponer el dataframe
    df = df.T
    return df.to_dict(orient='index')["Ahorros"]

def total_income_monthly(df: pd.DataFrame) -> float:
    """
    Función que devuelve el importe total de ingresos a lo largo del año

    :param df: dataframe con los datos
    :type df: pd.DataFrame
    :return: importe total de ingresos a lo largo del año
    :rtype: float
    """
    df = df.T
    return df.to_dict(orient='index')["Gastos"]

def get_df_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Función que devuelve el dataframe con los datos del año con los ingresos y gastos de cada mes

    :param df: dataframe con los datos del archivo
    :type df: pd.DataFrame
    :return: dataframe con los datos del año con los ingresos y gastos de cada mes
    :rtype: pd.DataFrame
    """
    dict_year = {}
    for col in df.columns:
        income_values = []
        spent_values = []
        for value in df[col]:
            if value > 0:
                income_values.append(value)
            else:
                spent_values.append(value)
        dict_year[col] = [
            sum(income_values), 
            abs(sum(spent_values))
        ]
    df_year = pd.DataFrame(dict_year)
    df_year = df_year.T
    df_year.columns = ['Ahorros', 'Gastos']
    return df_year

def draw_plot(df: pd.DataFrame) -> None:
    """
    Función que dibuja el gráfico de lineas con los ingresos y gastos de cada mes

    :param df: dataframe con los datos a dibujar
    :type df: pd.DataFrame
    :return: None
    """
    df.plot(kind='line', y=['Ahorros', 'Gastos'])
    plt.ylabel('Importe')
    plt.xlabel('Mes')
    plt.show()

def main():
    """
    Función principal que ejecuta el programa
    """
    # Carga del archivo
    filepath = Path(input("Ingrese la ruta del archivo: "))
    #filepath = Path(__file__).absolute().parent / 'finanzas2020.csv'
    # Lectura del archivo
    df = read_file(filepath)
    if df is None:
        return
    check_columns(df)
    df_year = get_df_year(parse_dataframe(df))
    # Imprimir el mes con mayor gasto y el importe total de ese mes
    month, spent = most_spent_month(df_year)
    print("===== MES CON MAYOR GASTO =====")
    print(f"El mes con mayor gasto es {month} y el importe total de gastos es {spent:.2f}\n")
    # Imprimir el mes con menor gasto y el importe total de ese mes
    month, saved = most_saving_month(df_year)
    print("===== MES CON MAYOR INGRESOS =====")
    print(f"El mes con menor gasto es {month} y el importe total de ingresos es {saved:.2f}\n")
    # Imprimir el importe medio de gastos de todo el año
    avg = avg_spent(df_year)
    print("===== IMPORTE MEDIO DE GASTOS AL AÑO =====")
    print(f"El importe medio de gastos de todo el año es {avg:.2f}\n")
    # Imprimir el importe total de gastos a lo largo del año
    total = total_spent_monthly(df_year)
    print("===== IMPORTE TOTAL DE GASTOS A LO LARGO DEL AÑO =====")
    tmp ="El importe total de gastos a lo largo del año es el siguiente:\n"
    for month, spent in total.items():
        tmp += f"    * {month}: {spent:.2f}\n"
    print(tmp)
    # Imprimir el importe total de ingresos a lo largo del año
    income = total_income_monthly(df_year)
    print("===== IMPORTE TOTAL DE INGRESOS A LO LARGO DEL AÑO =====")
    tmp ="El importe total de ingresos a lo largo del año es el siguiente:\n"
    for month, income in income.items():
        tmp += f"    * {month}: {income:.2f}\n"
    print(tmp)
    # Dibujar el gráfico de barras con los ingresos y gastos de cada mes
    
    draw_plot(df_year)

# Descomentar funcion para ejecutar con streamlit

def main_st():
    """
    Función principal que ejecuta el programa con streamlit
    """
    st.write("# Actividad 1 - BPP - Víctor Luque")
    st.write("## Control de errores, pruebas y validación de datos")
    # Carga del archivo
    # filepath comes from input
    file = st.file_uploader("Ingrese el archivo", type=['csv'])
    if file is not None:
    #filepath = Path(__file__).absolute().parent / 'finanzas2020.csv'
    # Lectura del archivo
        df = pd.read_csv(file, sep='\t')
        check_columns(df)
        df_year = get_df_year(parse_dataframe(df))
        # Imprimir el mes con mayor gasto y el importe total de ese mes
        month, spent = most_spent_month(df_year)
        st.write(f"El mes con mayor gasto es `{month}` y el importe total de gastos es `{spent:.2f} €`\n")
        month, saved = most_saving_month(df_year)
        st.write(f"El mes con menor gasto es `{month}` y el importe total de ingresos es `{saved:.2f} €`\n")
        avg = avg_spent(df_year)
        st.write(f"El importe medio de gastos de todo el año es `{avg:.2f} €`\n")
        st.write(f"El importe total de gastos y ahorros a lo largo del año es:")
        st.table(df_year)
        st.write(f"La gráfica de los gastos y ahorros a lo largo del año es:")
        df_year["fecha"] = df_year.index.copy()
        # Add 2020 to each fecha
        df_year["fecha"] = df_year["fecha"].apply(lambda x: f"2020-{x}")
        df_year['fecha'] = pd.to_datetime(df_year['fecha'], format='%Y-%B')
        base = alt.Chart(df_year).mark_bar().encode(x='month(fecha):O')
        a = base.mark_line(color="#00ff00", point=True).encode(alt.Y('Ahorros', axis=alt.Axis(title='Cantidad')))
        b = base.mark_line(color="#ff0000", point=True).encode(alt.Y('Gastos'))
        c = base.mark_text(dy=-15, color="white").encode(alt.Y("Ahorros"), alt.Text("Ahorros"))
        d = base.mark_text(dy=-15, color="white").encode(alt.Y("Gastos"), alt.Text("Gastos"))
        ab = alt.layer(a,b)
        cd = alt.layer(c,d)
        final = alt.layer(ab,cd)
        st.altair_chart(final, use_container_width=True)
 

if __name__ == '__main__':
    # Descomentar linea para ejecutar con streamlit (streamlit run app_finanzas.py)
    main_st()
    # Descomentar linea para ejecutar localmente
    #main()
    