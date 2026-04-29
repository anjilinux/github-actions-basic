import mlflow
import os
import numpy as np

# get MLflow URL from environment
mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
mlflow.set_experiment("github-actions-exp")

print("🚀 Training started...")

data = np.random.rand(5)

with mlflow.start_run():
    for i in range(3):
        print(f"Epoch {i+1} complete")

    # fake accuracy
    accuracy = float(np.random.uniform(0.7, 0.95))

    # log to MLflow
    mlflow.log_param("epochs", 3)
    mlflow.log_metric("accuracy", accuracy)

    # save model locally
    with open("model.txt", "w") as f:
        f.write(str(data))

    # log artifact to MLflow
    mlflow.log_artifact("model.txt")

print("✅ Training + MLflow logging complete")
