import mlflow
import os

os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://127.0.0.1:9000"
os.environ["AWS_ACCESS_KEY_ID"] = "minioadmin"
os.environ["AWS_SECRET_ACCESS_KEY"] = "minioadmin"

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("minio_test")

with mlflow.start_run(run_name="artifact_test"):
    with open("test_artifact.txt", "w") as f:
        f.write("Vérification de la connexion MinIO.")
    mlflow.log_artifact("test_artifact.txt")

print("✅ Artefact logué. Vérifie MinIO → bucket mlflow-artifacts.")
