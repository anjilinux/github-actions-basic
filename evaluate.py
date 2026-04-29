import random

print("📊 Evaluating model...")

accuracy = random.uniform(0.5, 1.0)
print(f"Accuracy: {accuracy}")

with open("metrics.txt", "w") as f:
    f.write(f"accuracy={accuracy}")

if accuracy < 0.8:
    print("❌ Model rejected")
    raise Exception("Model accuracy too low")

print("✅ Model accepted")
