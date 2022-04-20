import pandas as pd
import json

def get_iris_resume():
    # Load dataset
    iris = pd.read_csv("iris.csv")
    # Resume df using describe method and conver to json as Index
    iris_describe = json.loads(
        iris.describe()\
        .to_json(orient="index")
    )
    return iris_describe