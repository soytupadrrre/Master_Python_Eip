import pandas as pd
import json
from .machine_learning import iris

def get_iris_resume():
    # Load dataset
    iris = pd.read_csv("iris.csv")
    # Resume df using describe method and convert to json as Index
    iris_describe = json.loads(
        iris.describe()\
        .to_json(orient="index")
    )
    return iris_describe

def get_iris_accuracy():
    response = {}
    iris_df = pd.read_csv("iris.csv")
    response["species"] = iris_df.species.value_counts().to_dict()
    results = iris.predict_results(iris_df)
    response["algorithms"] = []
    for result in results:
        template = {"name": result[3], "results": {
            "accuracy": result[2],
            "predicted": result[1],
            "real": result[0]
        }}
        response["algorithms"].append(template)
    return response

if __name__ == "__main__":
    print(get_iris_accuracy())
    print("\n\n")
    print(get_iris_resume())
    