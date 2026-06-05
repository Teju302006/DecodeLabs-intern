import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv(r"C:\Users\TejaswiniD\Downloads\archive (2)\employee_data.csv")

# Show first rows
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Check duplicate IDs
print("\nDuplicate IDs:")
print(df['ID'].duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Save cleaned dataset
df.to_csv("cleaned_employee_data.csv", index=False)

print("\nData cleaning completed successfully!")