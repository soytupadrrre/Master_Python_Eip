import streamlit as st
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from rest_iris import RestIris
import pandas as pd

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

def view(iris: RestIris):
    st.header("Dashboard de Machine Learning")
    st.image("static/images/machine_learning.jpg")

    click = st.radio("Selecciona un apartado:", ("Precisión", "Predicción"))

    if click == "Precisión":
        st.subheader("Precisión de los modelos")
        precision = iris.get_accuracy()
        dtc, rfc = precision["algorithms"]
        # Replace dtc['results']['predicted'] and dtc['results']['real'] integer values to iris species
        dtc_pred = list(map(iris_mapper, dtc['results']['predicted']))
        dtc_real = list(map(iris_mapper, dtc['results']['real']))
        # Create df with results['predicted'] and results['real']
        rfc_pred = list(map(iris_mapper, rfc['results']['predicted']))
        rfc_real = list(map(iris_mapper, rfc['results']['real']))
        labels = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
        st.subheader("Decision Tree Classifier")
        st.write(f"Precisión del algoritmo: {dtc['results']['accuracy']}")
        st.write(f"A continuación se muestra la matriz de confusion del algoritmo:")
        # Create colum sum to compare predicted and real
        st.pyplot(conf_matrix_fig(dtc_real, dtc_pred, labels, "Decision Tree Classifier"))
        # Show confusion matrix
        st.subheader("Random Forest Classifier")
        st.write(f"Precisión del algoritmo: {rfc['results']['accuracy']}")
        st.write(f"A continuación se muestra la matriz de confusion del algoritmo:")
        st.pyplot(conf_matrix_fig(rfc_real, rfc_pred, labels, "Random Forest Classifier"))

    elif click == "Predicción":
        st.subheader("Predicción de datos")
        col1, col2 = st.columns(2)
        with col1:
            sepal_length = st.number_input("Sepal Length (cm)", step=0.1, min_value=0.0, max_value=8.0)
            petal_length = st.number_input("Petal Length (cm)", step=0.1, min_value=0.0, max_value=8.0)
        with col2: 
            sepal_width = st.number_input("Sepal Width (cm)", step=0.1, min_value=0.0, max_value=8.0)
            petal_width = st.number_input("Petal Width (cm)", step=0.1, min_value=0.0, max_value=8.0)
        classifier = st.selectbox("Selecciona un algoritmo", ("DecisionTree", "RandomForest")) 
        if st.button("Predecir"):
            data = {
                "sepal_length": sepal_length,
                "sepal_width": sepal_width,
                "petal_length": petal_length,
                "petal_width": petal_width,
                "classifier": classifier
            }
            results = iris.post_predict(data)
            result = pd.Series(results, index=results.keys())
            # series to dataframe
            result = pd.DataFrame(result).transpose()
            # move id to first column
            first_col = result.pop("id")
            sixth_col = result.pop("predicted_species")
            result.insert(0, "id", first_col)
            result.insert(5, "predicted_species", sixth_col)

            #result = result.reindex(columns=["id"] + list(result.columns[:-1]))
            st.write(result)