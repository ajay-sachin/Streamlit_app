import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data (you can replace this with your own data)
data = {
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Sales': np.random.randint(50, 200, size=10),
    'Profit': np.random.randint(10, 50, size=10)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("Simple Data Display App")

# Display the data as a table
st.subheader("Data Table")
st.write(df)

# Display a line plot for Sales over Time
st.subheader("Sales Over Time")
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Sales'], marker='o', color='b', label='Sales')
ax.set_title("Sales Trend")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
ax.legend()
st.pyplot(fig)

# Display a bar plot for Profit
st.subheader("Profit Overview")
fig, ax = plt.subplots()
ax.bar(df['Date'], df['Profit'], color='g', label='Profit')
ax.set_title("Profit by Date")
ax.set_xlabel("Date")
ax.set_ylabel("Profit")
ax.legend()
st.pyplot(fig)
