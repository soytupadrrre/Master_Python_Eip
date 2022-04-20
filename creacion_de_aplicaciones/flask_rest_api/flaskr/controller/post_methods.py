import pandas as pd
import json
import csv

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