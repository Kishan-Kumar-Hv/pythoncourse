import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Sample data
categories = ["A", "B", "C", "D", "E"]
values = [10, 20, 15, 25, 30]

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Simple Dashboard", style={"textAlign": "center"}),

    # Dropdown to select graph type
    dcc.Dropdown(
        id="graph-type",
        options=[
            {"label": "Bar Graph", "value": "bar"},
            {"label": "Line Graph", "value": "line"}
        ],
        value="bar",  # Default value
        style={"width": "50%", "margin": "auto"}
    ),

    # Graph display
    dcc.Graph(id="graph-output")
])

# Callback to update the graph based on the dropdown selection
@app.callback(
    Output("graph-output", "figure"),
    [Input("graph-type", "value")]
)
def update_graph(graph_type):
    if graph_type == "bar":
        return go.Figure(
            data=[go.Bar(x=categories, y=values)],
            layout=go.Layout(title="Bar Graph", xaxis=dict(title="Category"), yaxis=dict(title="Values"))
        )
    else:
        return go.Figure(
            data=[go.Scatter(x=categories, y=values, mode="lines+markers")],
            layout=go.Layout(title="Line Graph", xaxis=dict(title="Category"), yaxis=dict(title="Values"))
        )
# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
