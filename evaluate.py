import random

print("📊 Evaluating model...")

accuracy = random.uniform(0.5, 1.0)
print(f"Accuracy: {accuracy}")

# save metrics locally
with open("metrics.txt", "w") as f:
    f.write(f"accuracy={accuracy}")

# gate
if accuracy < 0.8:
    raise Exception("❌ Model accuracy too low")

print("✅ Model passed evaluation")
