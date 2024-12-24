import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

data = pd.read_csv('languages.csv')

line_plot = px.line(data, x='Year', y=['Python', 'JavaScript', 'Java', 'C++'],
                    title='Programming Language Usage Over the Years',
                    labels={'value': 'Usage (%)', 'variable': 'Language'})
line_plot.update_traces(mode='lines+markers', hoverinfo='x+y+name')
line_plot.update_layout(
    showlegend=True,
    height=400,
    width=500,
    hovermode='x unified',
)

data_2024 = data[data['Year'] == 2024].drop('Year', axis=1)

bar_plot = px.bar(x=data_2024.columns, y=data_2024.values.flatten(),
                  title="Usage of Languages in 2024", labels={'x': 'Language', 'y': 'Usage (%)'})

bar_plot.update_traces(
    hoverinfo='x+y+text',
    marker=dict(
        color=data_2024.values.flatten(),
        colorscale='Viridis',
        colorbar=dict(title="Usage (%)")
    ),
    text=data_2024.values.flatten(),
    textposition='outside'
)

bar_plot.update_layout(
    height=400,
    width=500,
    xaxis_title='Language',
    yaxis_title='Usage (%)',
    hovermode='x unified',
    showlegend=False,
)

pie_plot = px.pie(values=data_2024.values.flatten(),
                  names=data_2024.columns,
                  title="Usage of Languages in 2024 (Least Used)")
pie_plot.update_traces(textinfo='percent+label', hoverinfo='label+percent')
pie_plot.update_layout(
    height=400,
    width=500,
    hovermode='x unified',
)

fig = make_subplots(rows=1, cols=3,
                    subplot_titles=("Programming Language Usage Over the Years",
                                    "Usage of Languages in 2024",
                                    "Usage of Languages in 2024 (Least Used)"),
                    column_widths=[0.33, 0.33, 0.33],
                    specs=[[{"type": "xy"}, {"type": "xy"}, {"type": "pie"}]])

fig.add_trace(line_plot.data[0], row=1, col=1)
fig.add_trace(line_plot.data[1], row=1, col=1)
fig.add_trace(line_plot.data[2], row=1, col=1)
fig.add_trace(line_plot.data[3], row=1, col=1)
fig.add_trace(bar_plot.data[0], row=1, col=2)
fig.add_trace(pie_plot.data[0], row=1, col=3)

fig.update_layout(
    title_text="Programming Language Usage and Analysis in 2024",
    showlegend=False,
    height=500,
    width=1500,
    hovermode='x unified'
)

fig.show()
