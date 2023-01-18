from dash import html, dcc 
import dash 
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc 
import pandas as pd 
import numpy as np 
import plotly.express as px 
from dash_bootstrap_templates import ThemeSwitchAIO

from app import * 
from components import dados_geral, estados, sidebar 


# ===== Layout ===== # 
content = html.Div(id='page-content')

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], sm=2),
        dbc.Col([
            content
        ], md=10)
    ])
], fluid=True)

# ===== Callback ===== #

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def render_page(pathname):
    if pathname == '/' or pathname == '/dados/geral':
        return dados_geral.layout
    if pathname == '/dados/estados':
        return estados.layout 

if __name__ == '__main__': 
    app.run_server(debug=True, port=8081)