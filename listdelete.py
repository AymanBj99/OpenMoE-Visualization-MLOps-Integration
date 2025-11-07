import mlflow

client = mlflow.tracking.MlflowClient()
experiments = client.list_experiments(view_type=mlflow.entities.ViewType.DELETED_ONLY)

for exp in experiments:
    print(f"ID: {exp.experiment_id} | Name: {exp.name} | Lifecycle: {exp.lifecycle_stage}")
