🌡 Temperature Data Analysis Project
📌 About the Project

This project analyzes daily temperature data from a CSV file and provides useful insights such as:

-Monthly average temperatures
-The top 5 hottest days of the year
-Overall temperature trends (line chart, bar charts, histogram)
-Option to download a combined trend chart as an image (.png)

It is designed to be interactive, letting users choose what kind of analysis they want to perform from a simple menu-driven interface.


⚠ Requirements

Before running this project, make sure your CSV file contains the following columns (with exact names):

-Year
-Month
-Day
-Temperature
🔹 Example format:
    Year	Month	Day	Temperature
    2023	  1	     1	   24.5
    2023	  1	     2	   25.1
    2023	  1	     3	   23.9

Note:The program will automatically generate a new column called    Temperature_linear using linear interpolation for missing values.


⚙ Installation
1. Make sure you have Python 3.x installed.
2. Install required dependencies by running:
    -pip install pandas numpy matplotlib
3. Save your dataset as a .csv file (with required columns).

▶ How to Use
1. Run the Python script:
    python temperature_analysis.py
2. Enter the path to your CSV file when prompted.
3. Enter the specific year you want to analyze.

Choose an option from the menu:
1. Average temperature per month
2. 5 hottest days
3. Overall trend
4. Download Overall Trend Chart
5. Exit

📊 Features
1️⃣ Average Temperature per Month
    Displays the monthly average temperatures.
2️⃣ 5 Hottest Days
    Finds the top 5 hottest days of the selected year.
3️⃣ Overall Trend
    Generates multiple plots in one window:
    - Line chart → Monthly average temperatures
    - Bar chart → Hottest day per month
    - Histogram → Temperature distribution
    - Bar chart → Coldest day per month
4️⃣ Download Trend Chart
    Saves the overall trend charts as Overall_Trend_Chart.png with high quality (dpi=300).


📂 Output Example
Console Output (Monthly Average Example):
Month
1    24.8
2    27.2
3    30.1
...
Saved Chart:
A 2×2 figure containing line chart, bar charts, and histogram of the year’s temperature trends.

✅ Exit
Choose option 5 to exit the program safely.

🚀 Future Improvements

    Support for multiple years comparison
    Adding precipitation / humidity analysis
    Export results as CSV/Excel report

👨‍💻 Author
    Developed by Asir Hamim