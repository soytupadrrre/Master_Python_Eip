import pandas as pd
import json

def delete_iris_last_row():
    # Read iris.csv
    iris = pd.read_csv("iris.csv")
    # Delete last row
    iris.drop(iris.index[-1], inplace=True)
    # Write to csv
    iris.to_csv("iris.csv", index=False)
    # Show last row as json oriented as index
    result = json.loads(
        iris.iloc[-1]\
        .to_json(orient="index")
    )
    return result

def delete_iris_by_id(data):
    data = json.loads(data)
    try: data["id"]
    except: return "Error: No id specified"
    # Read iris.csv
    iris = pd.read_csv("iris.csv")
    # Delete last row
    iris.drop(iris.index[data["id"] - 1], inplace=True)
    # Write to csv
    iris.to_csv("iris.csv", index=False)
    # Show last row as json oriented as index
    return "Deleted row with id: " + str(data["id"])