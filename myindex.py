from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from components import sidebar, dashboards
from app import *

# =========  Layout  =========== #
app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
        ], md=2),
        dbc.Col([
            dashboards.layout
        ], md=10)
    ])
], fluid=True,)

if __name__ == '__main__':
    app.run_server(debug=True)