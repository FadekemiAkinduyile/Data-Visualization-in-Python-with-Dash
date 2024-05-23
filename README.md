# Data-Visualization-in-Python-with-Dash

This project demonstrates how to visualize precious metals prices using Python, Streamlit, and Plotly. The dataset spans from 2018 to 2021 and includes prices for various metals such as Gold, Silver, Platinum, Palladium, Rhodium, Iridium, and Ruthenium. The primary objective is to provide an interactive web application that allows users to explore these prices over time.

**1. Data Loading and Preparation:**
   
The data is loaded from a CSV file named precious_metals_prices_2018_2021.csv.

Date formatting is inferred and converted to datetime objects for accurate plotting.


**2. Interactive Dashboard with Streamlit:**
   
The application uses Streamlit for creating the user interface.

Users can select a metal from a dropdown menu to visualize its price trends.

A date range selector allows users to filter the data within a specific time frame.


**3. Dynamic Plotting with Plotly:**
   
Plotly Express is used to create line charts for the selected metal.

The charts are dynamically updated based on user input for metal selection and date range.

Custom color mapping is applied to different metals for better visualization.

**Usage**

To run the application, ensure you have the necessary libraries installed:

pip install streamlit plotly pandas

Then, execute the Streamlit application:

requirements.txt

app.py

![image](https://github.com/FadekemiAkinduyile/Data-Visualization-in-Python-with-Dash/assets/102438301/34842116-d73f-4d3b-862b-654b24a67145)
