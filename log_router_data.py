import mlflow
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

# Config MLflow
mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
mlflow.set_experiment(os.getenv("MLFLOW_EXPERIMENT_NAME"))

with mlflow.start_run(run_name=os.getenv("MLFLOW_RUN_NAME")):
    # Exemple : log params du modèle
    mlflow.log_param("model_name", "google/switch-base-8")
    mlflow.log_param("num_layers", 12)
    mlflow.log_param("num_experts", 8)
    
    # Exemple : log métriques
    df = pd.read_csv("router_analysis.csv")
    mlflow.log_metric("avg_probability", df["probability"].mean())

    # Log du CSV comme artifact
    mlflow.log_artifact("router_analysis.csv")

print("✅ Données enregistrées dans MLflow avec succès !")
