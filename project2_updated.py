
import pandas as pd

# Load datasets
dataset1 = pd.read_excel("dataset_1.xlsx")
dataset2 = pd.read_excel("dataset_2.xlsx")
dataset3 = pd.read_excel("dataset_3.xlsx")

# Merge dataset1 and dataset2 on 'instant'
merged_df = pd.merge(dataset1, dataset2.drop(columns=['Unnamed: 0']), on='instant')

# Fill missing 'atemp' values with mean
merged_df['atemp'].fillna(merged_df['atemp'].mean(), inplace=True)

# Save merged dataset1 and dataset2
merged_df.to_excel("merged_dataset1_2.xlsx", index=False)

# Concatenate merged_df with dataset3
final_dataset = pd.concat([merged_df, dataset3], ignore_index=True)

# Save final cleaned dataset
final_dataset.to_excel("final_dataset_v2.xlsx", index=False)
