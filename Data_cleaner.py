import pandas as pd
import numpy as np

df=pd.read_csv("E:\Asir\Project1_Data_cleaner\Dhaka.csv")
#df['Temperature_linear'] = df['Temperature'].interpolate(method='linear')
specific_year = 2023
#print(df[df['Year'] == specific_year][['Temperature', 'Temperature_linear']])
#print(df[df['Year'] == specific_year].isnull().sum())
#df.to_csv("E:\Asir\Project1_Data_cleaner\Dhaka.csv", index=False)
missing_rows = df[df['Temperature'].isna() & (df['Year'] == specific_year)]

# Show Day, original Temperature, and interpolated Temperature
print(missing_rows[['Day', 'Temperature', 'Temperature_linear']])