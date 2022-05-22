from cProfile import label
import streamlit as st
import altair as alt
from rest_iris import RestIris
import pandas as pd
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

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

def iris_mapper(value: int) -> str:
    if value == 0:
        return "Iris-setosa"
    elif value == 1:
        return "Iris-versicolor"
    else:
        return "Iris-virginica"

def conf_matrix_fig(real, pred, labels, name):
    cm = confusion_matrix(real, pred, labels=labels)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(cm)
    plt.title('Matriz de confusion: ' + name)
    fig.colorbar(cax)
    ax.set_xticks([0,1,2])
    ax.set_yticks([0,1,2])
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, cm[i, j], va='center', ha='center', size="xx-large")
    plt.xlabel('Predecido')
    plt.ylabel('Verdadero')
    return fig

if add_radio == "Ver datos":
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
   
elif add_radio == "Ver Machine Learning":
    st.header("Dashboard de Machine Learning")
    st.image("static/images/machine_learning.jpg")
    st.subheader("Precisión de los modelos")


    click = st.button("Ver precisión")
    if click:
        precision = iris.get_accuracy()
        dtc, rfc = precision["algorithms"]
        st.success("Decision Tree Classifier")
        st.write(f"Precisión: {dtc['results']['accuracy']}")
        # create df with results['predicted'] and results['real']
        #df = pd.DataFrame({"predicted": dtc['results']['predicted'], "real": dtc['results']['real']})
        # Create colum sum to compare predicted and real
        # Show confusion matrix

        
        
        # Replace dtc['results']['predicted'] and dtc['results']['real'] integer values to iris species
        dtc_pred = list(map(iris_mapper, dtc['results']['predicted']))
        dtc_real = list(map(iris_mapper, dtc['results']['real']))
        # Create df with results['predicted'] and results['real']
        rfc_pred = list(map(iris_mapper, rfc['results']['predicted']))
        rfc_real = list(map(iris_mapper, rfc['results']['real']))
        labels = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
        
        st.pyplot(conf_matrix_fig(dtc_real, dtc_pred, labels, "Decision Tree Classifier"))
        st.pyplot(conf_matrix_fig(rfc_real, rfc_pred, labels, "Random Forest Classifier"))


        st.write("Random Forest Classifier")
        st.write(rfc)
            
        
    

