import pandas as pd

df = pd.read_csv("my_labels.csv")

labels = ["raid", "tackle", "bonus", "out", "idle"]

df["action"] = [labels[i % len(labels)] for i in range(len(df))]

df.to_csv("final_labels.csv", index=False)

print("Done! Balanced labels created")