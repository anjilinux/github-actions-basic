import mlflow
import os

mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
mlflow.set_experiment("github-actions-exp")

with mlflow.start_run():
    mlflow.log_param("epochs", 3)
    mlflow.log_metric("accuracy", 0.9)

print("✅ Logged to MLflow")
