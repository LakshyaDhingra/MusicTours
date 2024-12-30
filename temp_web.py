import streamlit as st
import plotly.express as fx
import sqlite3

connection = sqlite3.connect("temp_data.db")


def read_date():
    cursor = connection.cursor()
    cursor.execute("SELECT date FROM weather")
    rows = cursor.fetchall()
    return rows


def read_temp():
    cursor = connection.cursor()
    cursor.execute("SELECT temperature FROM weather")
    rows = cursor.fetchall()
    return rows


st.title("Live Temperature")

dates = read_date()
temperatures = read_temp()


dates = [d[0] for d in dates]
temperatures = [t[0] for t in temperatures]

figure = fx.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperatures"})
st.plotly_chart(figure)
