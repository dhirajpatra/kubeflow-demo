import joblib
import sys
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn

def train(input_path: str):
    # Load preprocessed data
    X_train, X_test, y_train, y_test = joblib.load(input_path)

    # Train model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # Evaluate and log with MLflow
    acc = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, "model")

if __name__ == "__main__":
    input_path = sys.argv[1]  # path to input artifact from preprocess
    train(input_path)
