from minio import Minio

# Connexion à ton serveur MinIO
client = Minio(
    "127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

bucket_name = "mlflow-artifacts"

# 1️⃣ Supprimer tous les fichiers à l'intérieur
objects = client.list_objects(bucket_name, recursive=True)
for obj in objects:
    client.remove_object(bucket_name, obj.object_name)
    print(f"Supprimé : {obj.object_name}")

# 2️⃣ Supprimer le bucket lui-même
client.remove_bucket(bucket_name)
print(f"Bucket '{bucket_name}' supprimé avec succès !")
