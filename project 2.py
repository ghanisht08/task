import pandas as pd

df =pd.read_csv('/Users/ghanishtrajoria/Documents/01.Data Cleaning and Preprocessing.csv')

print(df)

print(df.head())

print(df.tail())

# Filter data based on condition
filtered_df = df[df['ChipRate'] > 30]
print(filtered_df.head())

# Handle missing values
cleaned_df =df.dropna()
print(cleaned_df.head())

# Calculate summary statistics
summary_stats = df.describe()
print(summary_stats)
