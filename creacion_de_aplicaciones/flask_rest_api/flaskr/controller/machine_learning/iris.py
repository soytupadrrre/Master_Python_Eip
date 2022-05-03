from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def __revert_mapping(y):
    if y == 0:
        return "setosa"
    elif y == 1:
        return "versicolor"
    elif y == 2:
        return "virginica"
    else:
        return "unknown"

def predict_results(df_train, df_test=None, classifier='DecissionTree'):
    # Carga de datos
    X_train = df_train.drop(["id", 'species'], axis=1)
    df_train.species = df_train.species.map({'setosa': 0, 'versicolor': 1, 'virginica': 2})
    y_train = df_train["species"]
    
    # Comprobación de df_test, en caso de que no exista, se usa df_train y se divide en train y test
    if df_test is not None:
        X_train = X_train.values
        X_test = df_test.values
        y_train = y_train.values
        # Lanzamiento de predicciones
        if classifier.lower() == 'decissiontree':
            results = run_decision_tree(X_train, X_test, y_train)
        elif classifier.lower() == 'randomforest':
            results = run_random_forest(X_train, X_test, y_train)
        else:
            return "Invalid classifier"
    else:
        results = []
        X = df_train.values
        y = y_train.values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        # Lanzamiento de predicciones
        results.append(run_decision_tree(X_train, X_test, y_train, y_test))
        results.append(run_random_forest(X_train, X_test, y_train, y_test))
    return results

def run_decision_tree(X_train, X_test, y_train, y_test=None):
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    # En caso de no contar con y_test, se devuelve el resultado de la predicción
    if y_test is not None:
        score = clf.score(X_test, y_test)
        return str(y_test.tolist()), str(y_pred.tolist()), score, "Decision Tree"
    return __revert_mapping(y_pred.tolist()[0]), "Decission Tree Classifier"

def run_random_forest(X_train, X_test, y_train, y_test=None):
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    # En caso de no contar con y_test, se devuelve el resultado de la predicción
    if y_test is not None:
        score = clf.score(X_test, y_test)
        return str(y_test.tolist()), str(y_pred.tolist()), score, "Random Forest"
    return __revert_mapping(y_pred.tolist()[0]), "Random Forest Classifier"
    
if __name__ == "__main__":
    import pandas as pd
    df_train = pd.read_csv("iris.csv")
    df_test = pd.DataFrame({
                            "sepal_length": [4.5],
                            "sepal_width": [3.3],
                            "petal_length": [3.2],
                            "petal_width": [2.5]})
    results = predict_results(df_train, df_test)

    #results = obtain_results(pd.read_csv("iris.csv"))
    print(results)