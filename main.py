import pandas as pd

# Load dataset (YOUR file name)python main.py
df = pd.read_csv("dataset/dataset_metadata.csv", sep="\t")

print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nTotal rows:")
print(len(df))