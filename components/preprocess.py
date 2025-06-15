import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import joblib
import sys

def preprocess(output_path: str):
    iris = load_iris(as_frame=True)
    df = iris.frame
    X = df.drop("target", axis=1)
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    joblib.dump((X_train, X_test, y_train, y_test), output_path)

if __name__ == "__main__":
    output_path = sys.argv[1]
    preprocess(output_path)
