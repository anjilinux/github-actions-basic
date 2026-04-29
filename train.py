import os
import mlflow
import numpy as np

# 🔥 FORCE FIX (critical)
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
os.environ["MLFLOW_HTTP_REQUEST_HEADER_ngrok-skip-browser-warning"] = "true"

mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
mlflow.set_experiment("github-actions-exp")

print("🚀 Training started...")

data = np.random.rand(5)

with mlflow.start_run():
    for i in range(3):
        print(f"Epoch {i+1} complete")

    accuracy = float(np.random.uniform(0.7, 0.95))

    mlflow.log_param("epochs", 3)
    mlflow.log_metric("accuracy", accuracy)

    with open("model.txt", "w") as f:
        f.write(str(data))

    mlflow.log_artifact("model.txt")

print("✅ Training + MLflow logging complete")
