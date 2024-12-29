import streamlit as st
import plotly.express as fx
import pandas as pd

st.title("Live Temperature")
df = pd.read_csv("temp_data.txt")

with open("temp_data.txt", "r") as file:
    content = file.read()
dates = df["date"]
temperatures = df["temperature"]

figure = fx.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperatures"})
st.plotly_chart(figure)
