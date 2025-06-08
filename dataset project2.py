import pandas as pd
import numpy as np

# --------------------
# Step 1: Load Dataset 1 and perform basic checks
# --------------------
df1 = pd.read_excel('/mnt/data/dataset_1.xlsx')
print("Dataset 1 - Head:\n", df1.head())
print("Dataset 1 - Missing Values:\n", df1.isnull().sum())
print("Dataset 1 - Duplicate Rows:", df1.duplicated().sum())
print("Dataset 1 - Data Types:\n", df1.dtypes)

# --------------------
# Step 2: Load Dataset 2 and perform basic checks
# --------------------
df2 = pd.read_excel('/mnt/data/dataset_2.xlsx')
print("Dataset 2 - Head:\n", df2.head())
print("Dataset 2 - Missing Values:\n", df2.isnull().sum())
print("Dataset 2 - Duplicate Rows:", df2.duplicated().sum())
print("Dataset 2 - Data Types:\n", df2.dtypes)

# --------------------
# Step 3: Merge Dataset 1 and Dataset 2 using merge or concat
# --------------------
merged_12 = pd.merge(df1, df2, how='outer')
print("Merged Dataset 1 & 2 - Shape:", merged_12.shape)
print("Merged Dataset 1 & 2 - Missing Values:\n", merged_12.isnull().sum())
print("Merged Dataset 1 & 2 - Duplicates:", merged_12.duplicated().sum())

# --------------------
# Step 4: Load Dataset 3 and perform basic checks
# --------------------
df3 = pd.read_excel('/mnt/data/dataset_3.xlsx')
print("Dataset 3 - Head:\n", df3.head())
print("Dataset 3 - Missing Values:\n", df3.isnull().sum())
print("Dataset 3 - Duplicate Rows:", df3.duplicated().sum())
print("Dataset 3 - Data Types:\n", df3.dtypes)

# --------------------
# Step 5: Check merged_12 dataset again before combining with Dataset 3
# --------------------
print("Merged Dataset 1 & 2 - Data Types:\n", merged_12.dtypes)

# --------------------
# Step 6: Merge merged_12 with Dataset 3
# --------------------
final_data = pd.merge(merged_12, df3, how='outer')
print("Final Dataset - Shape:", final_data.shape)
print("Final Dataset - Missing Values:\n", final_data.isnull().sum())
print("Final Dataset - Duplicates:", final_data.duplicated().sum())

# --------------------
# Step 7: Handle Outliers (example using IQR for temp)
# --------------------
Q1 = final_data['temp'].quantile(0.25)
Q3 = final_data['temp'].quantile(0.75)
IQR = Q3 - Q1
outliers = final_data[(final_data['temp'] < Q1 - 1.5 * IQR) | (final_data['temp'] > Q3 + 1.5 * IQR)]
print("Outliers in Temp Column:", outliers.shape[0])

# --------------------
# Step 8: Check Correlation and Skewness
# --------------------
print("Correlation Matrix:\n", final_data.corr(numeric_only=True))
print("Skewness:\n", final_data.skew(numeric_only=True))

# --------------------
# Step 9: Save final cleaned data
# --------------------
final_data.to_csv('final_cleaned_dataset.csv', index=False)

