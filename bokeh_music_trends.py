import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

df = pd.read_csv('languages.csv')

def create_bar_chart():
    max_usage = df.mean().iloc[1:].idxmax()
    max_usage_value = df.mean().iloc[1:].max()
    fig = go.Figure([go.Bar(x=[max_usage], y=[max_usage_value])])
    fig.update_layout(
        xaxis_title='Programming Languages',
        yaxis_title='Average Usage (%)',
        height=400,
        width=600
    )
    return fig

def create_pie_chart():
    min_usage = df.mean().iloc[1:].idxmin()
    min_usage_value = df.mean().iloc[1:].min()
    fig = go.Figure(data=[go.Pie(labels=[min_usage], values=[min_usage_value])])
    fig.update_layout(
        height=400,
        width=600
    )
    return fig

def create_line_chart():
    fig = go.Figure()
    for column in df.columns[1:]:
        fig.add_trace(go.Scatter(x=df['Year'], y=df[column], mode='lines+markers', name=column))
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Usage (%)',
        height=400,
        width=600
    )
    return fig

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='chart-dropdown',
        options=[
            {'label': 'Most Used (Bar)', 'value': 'bar'},
            {'label': 'Least Used (Pie)', 'value': 'pie'},
            {'label': 'Usage Trend (Line)', 'value': 'line'}
        ],
        value='line',
        style={'width': '50%'}
    ),
    dcc.Graph(id='chart', style={'width': '100%', 'height': '500px'})
])

@app.callback(
    Output('chart', 'figure'),
    [Input('chart-dropdown', 'value')]
)
def update_chart(selected_chart):
    if selected_chart == 'bar':
        return create_bar_chart()
    elif selected_chart == 'pie':
        return create_pie_chart()
    elif selected_chart == 'line':
        return create_line_chart()

if __name__ == '__main__':
    app.run_server(debug=True)
