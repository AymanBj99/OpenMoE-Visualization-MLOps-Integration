import mlflow
from minio import Minio
import os

# ----------------------------
# 🔧 1️⃣ Configuration de MinIO
# ----------------------------
client = Minio(
    "127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

bucket_name = "mlflow-artifacts"
if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)
    print(f"✅ Bucket '{bucket_name}' créé avec succès.")
else:
    print(f"ℹ️ Bucket '{bucket_name}' déjà existant.")

# ----------------------------
# ⚙️ 2️⃣ Configuration de MLflow
# ----------------------------
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://127.0.0.1:9000"
os.environ["AWS_ACCESS_KEY_ID"] = "minioadmin"
os.environ["AWS_SECRET_ACCESS_KEY"] = "minioadmin"
os.environ["MLFLOW_TRACKING_URI"] = "http://127.0.0.1:5000"

mlflow.set_experiment("switch_transformer_routing")

# ----------------------------
# 📦 3️⃣ Lancer un run MLflow
# ----------------------------
with mlflow.start_run(run_name="router_analysis_tracking"):
    # 🔹 Exemple : log d’un paramètre
    mlflow.log_param("model_name", "google/switch-base-8")

    # 🔹 Ton vrai fichier CSV
    csv_path = "data/router_analysis.csv"

    if os.path.exists(csv_path):
        mlflow.log_artifact(csv_path)
        print(f"✅ CSV '{csv_path}' enregistré avec succès dans MLflow + MinIO.")
    else:
        print("⚠️ Fichier router_analysis.csv introuvable.")

    # 🔹 Exemple : log d’un score de test
    mlflow.log_metric("test_accuracy", 0.97)
