import pandas as pd
import json

def update_iris_by_id(data):
    data = json.loads(data)
    # Check if id exists on request
    try: data["id"]
    except: return "Error: No id specified"
    # Read iris.csv
    iris = pd.read_csv("iris.csv")
    # Replace data as given in request
    # ID field is not editable
    iris.loc[iris["id"] == data["id"], "sepal_length"] = data["sepal_length"]
    iris.loc[iris["id"] == data["id"], "sepal_width"] = data["sepal_width"]
    iris.loc[iris["id"] == data["id"], "petal_length"] = data["petal_length"]
    iris.loc[iris["id"] == data["id"], "petal_width"] = data["petal_width"]
    iris.loc[iris["id"] == data["id"], "species"] = data["species"]
    # Write to csv
    iris.to_csv("iris.csv", index=False)
    # Show last row as json oriented as index
    result = json.loads(
        iris.iloc[-1]\
        .to_json(orient="index")
    )
    return result

def update_iris_last_row(data):
    # data to json
    data = json.loads(data)
    print("==========================")
    print(data)
    print("==========================")
    # Read iris.csv
    iris = pd.read_csv("iris.csv")
    # Get last id
    id = len(iris)
    # Replace data as given in request
    # ID field is not editable
    iris.loc[iris.index[-1], "id"] = id
    iris.loc[iris.index[-1], 'sepal_length'] = data['sepal_length']
    iris.loc[iris.index[-1], 'sepal_width'] = data['sepal_width']
    iris.loc[iris.index[-1], 'petal_length'] = data['petal_length']
    iris.loc[iris.index[-1], 'petal_width'] = data['petal_width']
    iris.loc[iris.index[-1], 'species'] = data['species']

    # Write to csv
    iris.to_csv("iris.csv", index=False)
    # Show last row as json oriented as index
    result = json.loads(
        iris.iloc[-1]\
        .to_json(orient="index")
    )
    return result