import pandas as pd
from sklearn.preprocessing import Imputer
df = pd.read_csv('Data.csv')
df
df.isnull().sum()
df.dropna()
# drop kolom spesifik yang mengandung NaN 
df.dropna(subset=['Age'])
df.iloc[:, 1:3]
imputer = Imputer(missing_values='NaN', strategy='mean', axis = 0)
df.iloc[:, 1:3] = imputer.fit_transform(df.iloc[:, 1:3])
df