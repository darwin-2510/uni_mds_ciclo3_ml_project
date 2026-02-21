import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import mlflow
import mlflow.sklearn

def train_model():
    # Cargar data ya procesada
    X_train = pd.read_csv("data/training/X_train.csv")
    y_train = pd.read_csv("data/training/y_train.csv").values.ravel()

    # Configuración de MLflow Tracking (Lección 4)
    mlflow.set_experiment("Credit_Risk_Experiment")
    
    with mlflow.start_run(run_name="RandomForest_Final"):
        n_estimators = 150
        model = RandomForestClassifier(n_estimators=n_estimators)
        model.fit(X_train, y_train)
        
        # Log de parámetros y modelo
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.sklearn.log_model(model, "credit_model")
        
        # Guardar localmente con Joblib (Lección 5)
        joblib.dump(model, "models/credit_model.joblib")
        print("Modelo entrenado y guardado en models/")

if __name__ == "__main__":
    train_model()