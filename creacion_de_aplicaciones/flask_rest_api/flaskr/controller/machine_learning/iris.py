from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def obtain_results(df):
    results = []
    # Leer datos de csv
    X = df.drop(["id", 'species'], axis=1)    

    # y, la salida, solamente la columna "Species"
    df.species = df.species.map({'setosa': 0, 'versicolor': 1, 'virginica': 2})
    y = df["species"]

    # Algunas veces es necesario para que no devuelvan errores posteriormente
    X = X.values
    y = y.values
    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # Append to list
    results.append(run_decision_tree(X_train, X_test, y_train, y_test))
    results.append(run_random_forest(X_train, X_test, y_train, y_test))
       
    return results

def run_decision_tree(X_train, X_test, y_train, y_test):
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    score = clf.score(X_test, y_test)
    return str(y_test.tolist()), str(y_pred.tolist()), score, "Decision Tree"

def run_random_forest(X_train, X_test, y_train, y_test):
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    score = clf.score(X_test, y_test)
    return str(y_test.tolist()), str(y_pred.tolist()), score, "Random Forest"

if __name__ == "__main__":
    import pandas as pd
    results = obtain_results(pd.read_csv("iris.csv"))
    print("")
    for result in results:
        print(f"Name: {result[3]}")
        print(f"Accuracy: {result[2]}"),
        print(f"Predicted: \t{result[1]}"),
        print(f"Real: \t\t{result[0]}")
        print("")