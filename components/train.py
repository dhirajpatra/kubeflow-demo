import joblib
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn

def train():
    X_train, X_test, y_train, y_test = joblib.load("/tmp/data.pkl")
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    acc = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, "model")

if __name__ == "__main__":
    train()
