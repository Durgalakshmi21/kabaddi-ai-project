import pandas as pd

df = pd.read_csv("dataset/my_labels.csv")

# Remove duplicates (keep first occurrence)
df = df.drop_duplicates(subset="clip_id", keep="first")

# Save cleaned file
df.to_csv("dataset/final_labels.csv", index=False)

print("✅ Cleaned dataset saved!")
print("Total rows:", len(df))