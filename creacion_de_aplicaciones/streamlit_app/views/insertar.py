import streamlit as st
import pandas as pd

from rest_iris import RestIris

def view(iris: RestIris):
    st.header("Dashboard de Insertar Datos")
    #st.image("static/images/insert.png")
    st.subheader("Insertar datos en la base de datos")
    # Get data from user
    col1, col2 = st.columns(2)
    with col1:
        sepal_length = st.number_input("Sepal Length (cm)", step=0.1, min_value=0.0, max_value=8.0)
        petal_length = st.number_input("Petal Length (cm)", step=0.1, min_value=0.0, max_value=8.0)
    with col2:
        sepal_width = st.number_input("Sepal Width (cm)", step=0.1, min_value=0.0, max_value=8.0)
        petal_width = st.number_input("Petal Width (cm)", step=0.1, min_value=0.0, max_value=8.0)
    species = st.selectbox("Species", ("setosa", "versicolor", "virginica"))
    # Insert data
    if st.button("Insertar datos"):
        data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
            "species": species
        }
        result = iris.post_data(data)
        st.success("Datos insertados correctamente")
        # result dict to dataframe
        result = pd.Series(result, index=result.keys())
        # series to dataframe
        result = pd.DataFrame(result).transpose()
        # move id to first column
        first_col = result.pop("id")
        result.insert(0, "id", first_col)
        st.write(result)