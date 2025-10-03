import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("E:\Asir\Project1_Data_cleaner\Dhaka.csv")
specific_year = 2023
df_Year=df[df['Year'] == specific_year]
df_Year['Temperature_linear'] = df_Year['Temperature'].interpolate(method='linear')
#print(df[df['Year'] == specific_year][['Temperature','Temperature_linear']])
#print(df[df['Year'] == specific_year].isnull().sum())
#df.to_csv("E:\Asir\Project1_Data_cleaner\Dhaka.csv", index=False)
#missing_rows = df[df['Temperature'].isna() & (df['Year'] == specific_year)]

# Show Day, original Temperature, and interpolated Temperature
#print(missing_rows[['Day', 'Temperature', 'Temperature_linear']])


def average_temperature_per_month():
    montly_avg = df_Year.groupby('Month')['Temperature_linear'].mean()
    print(montly_avg)

def five_hottest_days():
    find = df_Year.groupby(['Month','Day'])['Temperature_linear'].max()
    find_sorted=find.sort_values(ascending=False).head(5)
    print(find_sorted)

def overall_trend():
    fig,ax = plt.subplots(2,2,figsize=(12,8))
    #For Line Chart
    montly_avg = df_Year.groupby('Month')['Temperature_linear'].mean()
    ax[0,0].plot(montly_avg.index, montly_avg.values, color='blue', marker='o', linestyle='-', label='Monthly Avg')
    ax[0,0].set_title("Daily Temperature Trend")
    ax[0,0].set_xlabel("Month")
    ax[0,0].set_ylabel("Temperature (°C)")
    ax[0,0].set_xticks(range(1, 13))
    ax[0,0].set_yticks(range(19, 40, 2))
    ax[0,0].grid()
    #For Bar Chart
    find = df_Year.groupby(['Month'])['Temperature_linear'].max()
    ax[0,1].bar(find.index, find .values, color='orange', alpha=0.7,linewidth=0.8, label='Hottest Days')
    ax[0,1].set_xlabel("Month")
    ax[0,1].set_ylabel("Temperature (°C)")
    ax[0,1].set_xticks(range(1, 13))

    plt.tight_layout()
    plt.show()

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
