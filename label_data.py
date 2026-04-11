import pandas as pd

# Load your metadata
df = pd.read_csv("dataset/dataset_metadata.csv")

# Define actions
labels = ["raid", "tackle", "bonus", "out", "idle"]

# Assign labels (temporary auto labels)
df["action"] = [labels[i % len(labels)] for i in range(len(df))]

# Save new file
df.to_csv("dataset/final_labels.csv", index=False)

print("✅ Labels added successfully!")