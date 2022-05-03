import pandas as pd
import json
import csv
from .machine_learning import iris

def insert_iris_data(data):
    # Insert data to csv
    data = json.loads(data)
    with open("iris.csv", "a", newline='') as f:
        fieldnames = ["id", "sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # Calc id
        id = len(pd.read_csv("iris.csv")) + 1
        writer.writerow({
            "id": id,
            "sepal_length": data["sepal_length"],
            "sepal_width": data["sepal_width"],
            "petal_length": data["petal_length"],
            "petal_width": data["petal_width"],
            "species": data["species"]
        })
        data["id"] = id
    return data

def insert_predicted_data(data):
    data = json.loads(data)
    # Create DataFrame from data
    # Format: {sepal_length, sepal_width, petal_length, petal_width}
    df_test = pd.DataFrame({
        "sepal_length": [data["sepal_length"]],
        "sepal_width": [data["sepal_width"]],
        "petal_length": [data["petal_length"]],
        "petal_width": [data["petal_width"]]
    })
    # Read iris.csv
    df_train = pd.read_csv("iris.csv")
    # Run prediction
    predicted, classifier = iris.predict_results(df_train, df_test, classifier=data["predict_model"])
    # Store results in iris.csv
    with open("iris.csv", "a", newline='') as f:
        fieldnames = ["id", "sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({
            "id": len(df_train) + 1,
            "sepal_length": data["sepal_length"],
            "sepal_width": data["sepal_width"],
            "petal_length": data["petal_length"],
            "petal_width": data["petal_width"],
            "species": predicted
        })
    # Prepare response
    return {
        "id" : len(df_train)+1,
        "sepal_length": data["sepal_length"],
        "sepal_width": data["sepal_width"],
        "petal_length": data["petal_length"],
        "petal_width": data["petal_width"],
        "predict_species": predicted,
        "algorithm": classifier
    }
