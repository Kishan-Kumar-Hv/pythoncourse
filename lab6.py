import pandas as pd
import plotly.express as px


df = pd.read_csv("anotherweather.csv")  # Replace with your file path
fig = px.line(
    df,
    x="Date",
    y="Temparature",
    title="Temparature Over Time",
    labels={"Date": "Date", "Temparature": "Temparature (°C)"}
)
fig.show()