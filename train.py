print("🚀 Training started...")

for i in range(3):
    print(f"Epoch {i+1} complete")

# simulate model output
with open("model.txt", "w") as f:
    f.write("fake trained model v1")

print("✅ Training finished + model saved")
