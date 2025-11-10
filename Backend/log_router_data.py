import os
import mlflow
import pandas as pd
from minio import Minio


# Vérification des variables d’environnement
print("🔍 Vérification des variables d'environnement :")
print("MLFLOW_TRACKING_URI =", os.getenv("MLFLOW_TRACKING_URI"))
print("MLFLOW_S3_ENDPOINT_URL =", os.getenv("MLFLOW_S3_ENDPOINT_URL"))
print("AWS_ACCESS_KEY_ID =", os.getenv("AWS_ACCESS_KEY_ID"))
print("AWS_SECRET_ACCESS_KEY =", os.getenv("AWS_SECRET_ACCESS_KEY"))

#Connexion à MinIO et création du bucket si besoin
minio_client = Minio(
    "127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

bucket_name = "mlflow-artifacts"
if not minio_client.bucket_exists(bucket_name):
    minio_client.make_bucket(bucket_name)
    print(f" Bucket '{bucket_name}' créé avec succès !")
else:
    print(f"Bucket '{bucket_name}' déjà existant.")

#Chargement du fichier router_analysis.csv
csv_path = os.path.join(os.getcwd(), "data/router_analysis.csv")

if not os.path.exists(csv_path):
    print(" Fichier router_analysis.csv introuvable.")
    exit()

df = pd.read_csv(csv_path)
print(f" Fichier chargé avec {len(df)} lignes et {len(df.columns)} colonnes.")

#Calcul de quelques métriques utiles
mean_prob = df["probability"].mean()
max_prob = df["probability"].max()
unique_layers = df["layer_name"].nunique()
unique_experts = df["expert_index"].nunique()

print(f" Moyenne des probabilités : {mean_prob:.4f}")
print(f" Max des probabilités : {max_prob:.4f}")
print(f" Nombre de couches : {unique_layers}")
print(f" Nombre d'experts : {unique_experts}")

# Initialisation de MLflow
mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
mlflow.set_experiment("SwitchTransformer_Routing")


#Enregistrement du run MLflow
with mlflow.start_run(run_name="router_analysis"):
    # Enregistrer les métriques principales
    mlflow.log_metric("mean_probability", mean_prob)
    mlflow.log_metric("max_probability", max_prob)
    mlflow.log_param("unique_layers", unique_layers)
    mlflow.log_param("unique_experts", unique_experts)

    # Logguer le fichier CSV complet
    mlflow.log_artifact(csv_path)

print("\n Données de routage enregistrées avec succès dans MLflow et MinIO !")
print(" Vérifie sur : http://127.0.0.1:5000 (MLflow UI)")
print("🪣 Bucket MinIO : http://127.0.0.1:9001 (mlflow-artifacts)")
