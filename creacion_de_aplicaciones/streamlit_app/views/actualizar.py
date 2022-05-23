import streamlit as st
import pandas as pd
from rest_iris import RestIris

def view(iris: RestIris):
    st.header("Dashboard de Actualizar Datos")
    #st.image("static/images/update.png")
    st.subheader("Actualizar datos en la base de datos")
    # Get data from user
    id = st.number_input("ID", step=1, min_value=1)
    col1, col2 = st.columns(2)
    with col1:
        sepal_length = st.number_input("Sepal Length (cm)", step=0.1, min_value=0.0, max_value=8.0)
        petal_length = st.number_input("Petal Length (cm)", step=0.1, min_value=0.0, max_value=8.0)
    with col2:
        sepal_width = st.number_input("Sepal Width (cm)", step=0.1, min_value=0.0, max_value=8.0)
        petal_width = st.number_input("Petal Width (cm)", step=0.1, min_value=0.0, max_value=8.0)
    species = st.selectbox("Species", ("setosa", "versicolor", "virginica"))
    # Update data
    if st.button("Actualizar datos"):
        data = {
            "id": id,
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
            "species": species
        }
        result = iris.put_by_id(data)
        st.success("Datos actualizados correctamente")
        # result dict to dataframe
        result = pd.Series(result, index=result.keys())
        # series to dataframe
        result = pd.DataFrame(result).transpose()
        # move id to first column
        first_col = result.pop("id")
        result.insert(0, "id", first_col)
        st.write(result)