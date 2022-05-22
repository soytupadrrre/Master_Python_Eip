from math import trunc
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

class IrisML:
    """
    Clase para el manejo Machine Learning de Iris DataSet
    """
    def __init__(self, df_train:pd.DataFrame, df_test:pd.DataFrame=None, classifier:str='DecissionTree') -> None:
        """
        Constructor de la clase

        :param df_train: DataFrame con los datos de entrenamiento
        :type df_train: pd.DataFrame
        :param df_test: DataFrame con los datos de prueba
        :type df_test: pd.DataFrame
        :param classifier: Clasificador a utilizar
        :type classifier: str
        :return: None
        """
        self.df_train = df_train
        self.df_test = df_test
        self.classifier = classifier

    @staticmethod
    def revert_mapping(y:int or str) -> str:
        """
        Método para revertir el mapeo del resultado de la predicción

        :param y: Resultado de la predicción
        :type y: int
        :return: Nombre de la especie
        :rtype: str
        """
        if isinstance(y, int):
            if y == 0:
                return "setosa"
            elif y == 1:
                return "versicolor"
            elif y == 2:
                return "virginica"
            else:
                return "unknown"
        else:
            return y

    def predict_results(self) -> list:
        """
        Método para predecir los resultados de la clasificación

        :return: Resultados de la clasificación
        :rtype: list
        """
        # Carga de datos
        X_train = self.df_train.drop(["id", 'species'], axis=1)
        self.df_train.species = self.df_train.species.map({'setosa': 0, 'versicolor': 1, 'virginica': 2})
        y_train = self.df_train["species"]
        
        # Comprobación de df_test, en caso de que no exista, se usa df_train y se divide en train y test
        if self.df_test is not None:
            X_train = X_train.values
            X_test = self.df_test.values
            y_train = y_train.values
            # Lanzamiento de predicciones
            if self.classifier.lower() == 'randomforest':
                results = self.__run_random_forest(X_train, X_test, y_train)
            else:
                results = self.__run_decision_tree(X_train, X_test, y_train)
        else:
            results = []
            X = self.df_train.values
            y = y_train.values
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            # Lanzamiento de predicciones
            results.append(self.__run_decision_tree(X_train, X_test, y_train, y_test))
            results.append(self.__run_random_forest(X_train, X_test, y_train, y_test))
        return results

    def __run_decision_tree(self, X_train, X_test, y_train, y_test=None):
        """
        Método para lanzar la predicción de un clasificador de árboles de decisión

        :param X_train: Datos de entrenamiento
        :type X_train: array
        :param X_test: Datos de prueba
        :type X_test: array
        :param y_train: Resultados de entrenamiento
        :type y_train: array
        :param y_test: Resultados de prueba
        :type y_test: array
        :return: Resultados de la predicción
        :rtype: list
        """
        clf = DecisionTreeClassifier(random_state=42)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        # En caso de no contar con y_test, se devuelve el resultado de la predicción
        if y_test is not None:
            score = f"{trunc(clf.score(X_test, y_test)*100)}%"
            return y_test.tolist(), y_pred.tolist(), score, "Decision Tree"
        return self.revert_mapping(y_pred.tolist()[0]), "Decission Tree Classifier"

    def __run_random_forest(self, X_train, X_test, y_train, y_test=None):
        """
        Método para lanzar la predicción de un clasificador de árboles aleatorios
            
        :param X_train: Datos de entrenamiento
        :type X_train: array
        :param X_test: Datos de prueba
        :type X_test: array
        :param y_train: Resultados de entrenamiento
        :type y_train: array
        :param y_test: Resultados de prueba
        :type y_test: array
        :return: Resultados de la predicción
        :rtype: list
        """

        clf = RandomForestClassifier()
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        # En caso de no contar con y_test, se devuelve el resultado de la predicción
        if y_test is not None:
            score = f"{trunc(clf.score(X_test, y_test)*100)}%"
            return y_test.tolist(), y_pred.tolist(), score, "Random Forest"
        return self.revert_mapping(y_pred.tolist()[0]), "Random Forest Classifier"
    
class RestIris:
    """
    Clase para el manejo de la API de Iris DataSet
    """
    def __init__(self, iris_path:str = "data/iris.csv") -> None:
        """
        Constructor de la clase

        :param iris_path: Path del dataset
        :type iris_path: str
        :return: None
        """
        self.iris_path = iris_path
        self.iris_df = pd.read_csv(self.iris_path, engine='python') 

    def update_csv(self) -> None:
        """
        Método para actualizar el csv
        """
        self.iris_df.to_csv(self.iris_path, index=False)

    def get_summary(self) -> dict:
        """
        Método para obtener el resumen del dataset
        
        :return: Resumen del dataset
        :rtype: dict
        """
        return self.iris_df.describe()

    def get_data(self) -> dict:
        """
        Método para obtener los datos del dataset

        :return: Datos del dataset
        :rtype: dict
        """
        return self.iris_df

    def get_accuracy(self) -> dict:
        """
        Método para obtener la precisión del dataset

        :return: Precisión del dataset
        :rtype: dict
        """
        response = {}
        # Es necesario leer el dataset cada vez que se quiera obtener la precisión
        iris_ml = IrisML(pd.read_csv(self.iris_path))
        response["species"] = self.iris_df.species.value_counts().to_dict()
        # Obtención de los resultados de las predicciones
        results = iris_ml.predict_results()
        response["algorithms"] = []
        for result in results:
            y_test, y_pred, score, classifier = result
            tmp = {"name": classifier, "results": {
                "accuracy": score,
                "predicted": y_pred,
                "real": y_test
            }}
            response["algorithms"].append(tmp)
        return response

    def post_data(self, data:dict) -> dict:
        """
        Método para guardar los datos de prueba
        
        :param data: Datos de prueba
        :type data: dict
        :return: Resultados de la predicción
        :rtype: dict
        """
        new_id = len(self.iris_df)+1
        data["id"] = new_id
        # Uso de pd.concat() para insertar los datos en el dataset
        # Metodo pd.append() funciona igual pero quedará obsoleto 
        # en proximas versiones de pandas

        del data["classifier"]
        self.iris_df = pd.concat([self.iris_df, pd.DataFrame(data, index=[new_id])])
        self.update_csv()
        data["id"] = new_id
        return data

    def post_predict(self, data:dict) -> dict:
        """
        Método para predecir los datos de prueba

        :param test_df: Datos de prueba
        :type test_df: pd.DataFrame
        :return: Resultados de la predicción
        :rtype: dict
        """
        test_df = pd.DataFrame({
            "sepal_length": [data["sepal_length"]],
            "sepal_width": [data["sepal_width"]],
            "petal_length": [data["petal_length"]],
            "petal_width": [data["petal_width"]]
        })
        # Run prediction
        iris_ml = IrisML(pd.read_csv(self.iris_path), test_df, data["classifier"])
        predicted, classifier = iris_ml.predict_results()
        # Store results in iris.csv
        new_id = len(self.iris_df) + 1
        self.iris_df = pd.concat([self.iris_df, pd.DataFrame({
            "id": [new_id],
            "sepal_length": [data["sepal_length"]],
            "sepal_width": [data["sepal_width"]],
            "petal_length": [data["petal_length"]],
            "petal_width": [data["petal_width"]],
            "species": [predicted],
        }, index=[new_id])])
        # Write to csv
        self.iris_df["species"] = IrisML.revert_mapping(self.iris_df["species"])
        self.update_csv()
        data["id"] = new_id
        data["predicted_species"] = predicted
        data["predicted_model"] = classifier
        return data
    
    def put_by_id(self, data:dict) -> dict:
        """
        Método para actualizar los datos de iris a partir de un id de fila
        
        :param data: Datos de prueba
        :type data: dict
        :return: Resultados de la predicción
        :rtype: dict
        """
        try: data["id"]
        except: return "Error: No id specified"
        # Replace data as given in request
        # ID field is not editable
        self.iris_df.loc[self.iris_df["id"] == data["id"], "sepal_length"] = data["sepal_length"]
        self.iris_df.loc[self.iris_df["id"] == data["id"], "sepal_width"] = data["sepal_width"]
        self.iris_df.loc[self.iris_df["id"] == data["id"], "petal_length"] = data["petal_length"]
        self.iris_df.loc[self.iris_df["id"] == data["id"], "petal_width"] = data["petal_width"]
        self.iris_df.loc[self.iris_df["id"] == data["id"], "species"] = data["species"]
        # Write to csv
        self.update_csv()
        return data

    def put_last_row(self, data:dict) -> dict:
        """
        Método para actualizar la ultima file de iris.csv

        :param data: Datos de prueba
        :type data: dict
        :return: Resultados de la predicción
        :rtype: dict
        """
        # Get last id
        last_id = len(self.iris_df)
        # Replace data as given in request
        # ID field is not editable
        self.iris_df.loc[self.iris_df["id"] == last_id, "sepal_length"] = data["sepal_length"]
        self.iris_df.loc[self.iris_df["id"] == last_id, "sepal_width"] = data["sepal_width"]
        self.iris_df.loc[self.iris_df["id"] == last_id, "petal_length"] = data["petal_length"]
        self.iris_df.loc[self.iris_df["id"] == last_id, "petal_width"] = data["petal_width"]
        self.iris_df.loc[self.iris_df["id"] == last_id, "species"] = data["species"]
        # Write to csv
        self.update_csv()
        return self.iris_df.iloc[-1].to_dict()
    
    def delete_last_row(self) -> None:
        """
        Método para eliminar la ultima fila de iris.csv

        :return: None
        :rtype: None
        """
        # Delete last row
        # iloc[rowstart:rowend, colstart:colend]
        self.iris_df = self.iris_df.iloc[:-1, :]
        # Write to csv
        self.update_csv()

    def delete_by_id(self, data:dict) -> str:
        """
        Método para eliminar una fila de iris.csv a partir de un id

        :param data: Datos de prueba
        :type data: dict
        :return: Resultados de la predicción
        :rtype: str
        """
        try: data["id"]
        except: return "Error: No id specified"
        # Delete row with given id
        self.iris_df = self.iris_df[self.iris_df["id"] != data["id"]]
        # Update ids
        self.iris_df["id"] = range(1, len(self.iris_df)+1)
        # Write to csv
        self.update_csv()
        # Show last row as json oriented as index
        return int(data["id"])
