import numpy as np

print("🚀 Training started...")

# fake training
data = np.random.rand(5)

for i in range(3):
    print(f"Epoch {i+1} complete")

# save model (dummy file)
with open("model.txt", "w") as f:
    f.write(str(data))

print("✅ Training finished + model saved")
