from pywebio import output
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from PIL import Image
import io
from rest_iris import RestIris
from pywebio import config
from app import helper

dtc, rtc = RestIris().get_accuracy()["algorithms"]

def iris_mapper(value: int) -> str:
        if value == 0:
            return "Iris-setosa"
        elif value == 1:
            return "Iris-versicolor"
        else:
            return "Iris-virginica"

def ver_precision_dtc():
    y_pred = list(map(iris_mapper, dtc['results']['predicted']))
    y_true = list(map(iris_mapper, dtc['results']['real']))
    return crear_img(y_pred, y_true, "Decission Tree")

def ver_precision_rfc():
    y_pred = list(map(iris_mapper, rtc['results']['predicted']))
    y_true = list(map(iris_mapper, rtc['results']['real']))
    return crear_img(y_pred, y_true, "Random Forest")

def crear_img(y_pred, y_true, name):
    labels = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(cm)
    plt.title('Matriz de confusion: ' + name + " Classifier")
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
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img = Image.open(buf)
    return img

@config(title="Matriz Confusion", description="Muestra la precision de los clasificadores")
def app_matrix():
    """
    Muestra la precision de los clasificadores utilizando una matriz de confusion
    """
    helper.menu()
    output.span(output.put_markdown("## Sección Machine Learning (Matriz de Confusion)"))
    output.put_markdown(f"### Precisión Decission Tree: {dtc['results']['accuracy']}")
    output.put_image(ver_precision_dtc())
    output.put_markdown(f"### Precisión Random Forest: {rtc['results']['accuracy']}")
    output.put_image(ver_precision_rfc())