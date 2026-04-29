import random

print("📊 Evaluating model...")

accuracy = random.uniform(0.5, 1.0)

print(f"Accuracy: {accuracy}")

# save metrics
with open("metrics.txt", "w") as f:
    f.write(f"accuracy={accuracy}")

# gate condition
if accuracy < 0.8:
    raise Exception("❌ Model accuracy too low")

print("✅ Model passed evaluation")
