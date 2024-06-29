import pandas as pd

# create a sample dataset
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [16, 17, 18, 20, 19],
        'Grade': [85, 90, 78, 92, 88]}
df = pd.DataFrame(data)

# filter out students who are older than 18 years old
filtered_df = df[df['Age'] <= 18]

print(filtered_df)

import pandas as pd
import numpy as np

# create a sample dataset with missing values
data = {'Score': [90, 80, np.nan, 70, 95],
        'Grade': [83, 95, 78, 97, 82]}
df = pd.DataFrame(data)

# fill missing values with the mean of the existing values
df['Score'].fillna(df['Score'].mean(), inplace=True)

print(df)

import pandas as pd

# create a sample dataset
data = {'Score': [90, 80, 70, 95, 85]}

df = pd.DataFrame(data)

# calculate summary statistics
summary_stats = df['Score'].describe()

print(summary_stats)
