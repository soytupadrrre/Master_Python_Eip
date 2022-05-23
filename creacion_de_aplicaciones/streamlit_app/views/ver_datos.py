import streamlit as st
from rest_iris import RestIris

def mapping(options):
    if options == "Conteo":
        return "count"
    elif options == "Media":
        return "mean"
    elif options == "Desviación":
        return "std"
    elif options == "Minimo":
        return "min"
    elif options == "Maximo":
        return "max"
    else:
        return options


def view(iris: RestIris):
    st.header("Dashboard de Datos")
    st.image("static/images/iris.png")
    st.subheader("Datos de Iris Dataset")
    data = iris.get_data()[["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]]
    data = data.rename(columns={
            "sepal_length": "Sepal L (cm)", 
            "sepal_width": "Sepal W (cm)", 
            "petal_length": "Petal L (cm)", 
            "petal_width": "Petal W (cm)", 
            "species": "Species"
        })
    st.dataframe(data)
    st.subheader("Resumen de datos")
    options = st.multiselect("Selecciona una opción", ("Conteo", "Media", "Desviación", "Minimo", "Maximo", "25%", "50%", "75%"))
    if options:
        options = list(map(mapping, options))
        summary = iris.get_summary()
        
        # Remove id column
        summary.drop(columns=["id"], inplace=True)
        summary.rename(columns={
            "sepal_length": "Sepal Length (cm)", 
            "sepal_width": "Sepal Width (cm)", 
            "petal_length": "Petal Length (cm)", 
            "petal_width": "Petal Width (cm)", 
            "species": "Species"
        }, inplace=True)
        summary = summary.loc[options]
        # invert columns and rows
        summary = summary.transpose()
    
        # move index to columns
        st.bar_chart(summary)