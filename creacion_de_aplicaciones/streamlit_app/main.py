import streamlit as st
from rest_iris import RestIris
import views


st.set_page_config(page_title="Iris", page_icon="🌸")
iris = RestIris("data/iris.csv")
st.title("Víctor Luque - Iris Streamlit")
st.text("Aplicación con Streamlit para trabajar con Iris Dataset")
st.text("Escoge un dashboard desde el menú lateral para verlo!")

with st.sidebar:
    add_radio = st.radio(
        "Escoge un tipo de dashboard",
        (
            "Ver datos",
            "Ver Machine Learning",
            "Insertar datos",
            "Actualizar datos",
            "Eliminar datos",
        )
    )

if add_radio == "Ver datos":
    views.ver_datos.view(iris)
   
elif add_radio == "Ver Machine Learning":
    views.machine_learning.view(iris)

elif add_radio == "Insertar datos":
    views.insertar.view(iris)

elif add_radio == "Actualizar datos":
    views.actualizar.view(iris)

elif add_radio == "Eliminar datos":
    views.eliminar.view(iris)

