import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=======================================================")
print("⚠ WARNING:")
print("The CSV file should contain the following columns: Month, Day, and Temperature (or Temperature_linear).")
print("Data can be from any city, but column names must match exactly for the analysis to work correctly.")
print("=======================================================\n")

path=input("Enter the path of your CSV file: ")
df=pd.read_csv(path)
specific_year = int(input("Enter the specific year you want to analyze (e.g., 2023): "))
df_Year=df[df['Year'] == specific_year].copy()
df_Year['Temperature_linear'] = df_Year['Temperature'].interpolate(method='linear')



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
    ax[0,0].set_title("Monthly Average Temperature Trend")
    ax[0,0].set_xlabel("Month")
    ax[0,0].set_ylabel("Temperature (°C)")
    ax[0,0].set_xticks(range(1, 13))
    ax[0,0].set_yticks(range(19, 40, 2))
    ax[0,0].grid()
    #For Bar Chart
    find = df_Year.groupby(['Month'])['Temperature_linear'].max()
    ax[0,1].bar(find.index, find .values, color='orange', alpha=0.7,linewidth=0.8, label='Hottest Days')
    ax[0,1].set_title("Hottest Days per Month")
    ax[0,1].set_xlabel("Month")
    ax[0,1].set_ylabel("Temperature (°C)")
    ax[0,1].set_xticks(range(1, 13))
    #For Histogram
    ax[1,0].hist(df_Year['Temperature_linear'], bins=10, color='green', alpha=0.7, edgecolor='black')
    ax[1,0].set_title("Temperature Distribution")
    ax[1,0].set_xlabel("Temperature (°C)")
    ax[1,0].set_ylabel("Number of Days")
    
    #For Bar Chart
    find2 = df_Year.groupby(['Month'])['Temperature_linear'].min()
    ax[1,1].bar(find2.index, find2.values, color='green', alpha=0.7,linewidth=0.8, label='Hottest Days')
    ax[1,1].set_title("Coldest Days per Month")
    ax[1,1].set_xlabel("Month")
    ax[1,1].set_ylabel("Temperature (°C)")
    ax[1,1].set_xticks(range(1, 13))

    plt.tight_layout()
    plt.show()

def overall_trend_Download():
    fig,ax = plt.subplots(2,2,figsize=(12,8))
    #For Line Chart
    montly_avg = df_Year.groupby('Month')['Temperature_linear'].mean()
    ax[0,0].plot(montly_avg.index, montly_avg.values, color='blue', marker='o', linestyle='-', label='Monthly Avg')
    ax[0,0].set_title("Monthly Average Temperature Trend")
    ax[0,0].set_xlabel("Month")
    ax[0,0].set_ylabel("Temperature (°C)")
    ax[0,0].set_xticks(range(1, 13))
    ax[0,0].set_yticks(range(19, 40, 2))
    ax[0,0].grid()
    #For Bar Chart
    find = df_Year.groupby(['Month'])['Temperature_linear'].max()
    ax[0,1].bar(find.index, find .values, color='orange', alpha=0.7,linewidth=0.8, label='Hottest Days')
    ax[0,1].set_title("Hottest Days per Month")
    ax[0,1].set_xlabel("Month")
    ax[0,1].set_ylabel("Temperature (°C)")
    ax[0,1].set_xticks(range(1, 13))
    #For Histogram
    ax[1,0].hist(df_Year['Temperature_linear'], bins=10, color='green', alpha=0.7, edgecolor='black')
    ax[1,0].set_title("Temperature Distribution")
    ax[1,0].set_xlabel("Temperature (°C)")
    ax[1,0].set_ylabel("Number of Days")
    
    #For Bar Chart
    find2 = df_Year.groupby(['Month'])['Temperature_linear'].min()
    ax[1,1].bar(find2.index, find2.values, color='green', alpha=0.7,linewidth=0.8, label='Hottest Days')
    ax[1,1].set_title("Coldest Days per Month")
    ax[1,1].set_xlabel("Month")
    ax[1,1].set_ylabel("Temperature (°C)")
    ax[1,1].set_xticks(range(1, 13))

    plt.tight_layout()
    plt.savefig('Overall_Trend_Chart.png', dpi=300)
    print("Chart saved as 'Overall_Trend_Chart.png'")
    

while True:
    print("\nChoose an option:")
    print("1. Average temperature per month")
    print("2. 5 hottest days")
    print("3. Overall trend")
    print("4. Download Overall Trend Chart")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        average_temperature_per_month()
    elif choice == "2":
        five_hottest_days()
    elif choice == "3":
        overall_trend()
    elif choice == "4":
        overall_trend_Download()
    elif choice == "5":
        print("✅ Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
