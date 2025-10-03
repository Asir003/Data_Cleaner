import pandas as pd
import numpy as np

df=pd.read_csv("E:\Asir\Project1_Data_cleaner\Dhaka.csv")
df['Temperature_linear'] = df['Temperature'].interpolate(method='linear')
specific_year = 2023
#print(df[df['Year'] == specific_year][['Temperature', 'Temperature_linear']])
#print(df[df['Year'] == specific_year].isnull().sum())
#df.to_csv("E:\Asir\Project1_Data_cleaner\Dhaka.csv", index=False)
#missing_rows = df[df['Temperature'].isna() & (df['Year'] == specific_year)]

# Show Day, original Temperature, and interpolated Temperature
#print(missing_rows[['Day', 'Temperature', 'Temperature_linear']])

def average_temperature_per_month():
    montly_avg = df.groupby('Month')['Temperature_linear'].mean()
    print(montly_avg)

def five_hottest_days():
    find = df.groupby(['Month','Day'])['Temperature_linear'].max()
    find_sorted=find.sort_values(ascending=False).head(5)
    print(find_sorted)

def overall_trend():
    print("Showing overall trend...")

while True:
    print("\nChoose an option:")
    print("1. Average temperature per month")
    print("2. 5 hottest days")
    print("3. Overall trend")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        average_temperature_per_month()
    elif choice == "2":
        five_hottest_days()
    elif choice == "3":
        overall_trend()
    elif choice == "4":
        print("✅ Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
