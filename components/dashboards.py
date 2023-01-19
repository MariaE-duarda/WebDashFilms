from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from globals import *
from app import app

df = pd.read_csv('1400-filmes.csv')

card_icon = {
    "color": "white",
    "textAlign":"center",
    "fontSize": 30, 
    "margin":"auto",
}

# =========  Layout  =========== #
layout = dbc.Col([
       dbc.Row([
        dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph01')
                ], style={'margin-top': '15px', 'margin-left': '10px'}),
        ], width=4),
            dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph03')
                ], style={'margin-top': '15px'}),
        ], width=4),
            dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph05')
                ], style={'margin-top': '15px'}),
        ], width=4),
       ]), 

       dbc.Row([
        dbc.Col([
            dbc.Card([
                dcc.RangeSlider(0, 20, 1, value=[5, 15], id='my-range-slider'),
                html.Div(id='output-container-range-slider')
            ], style={'margin-top': '10px', 'margin-left': '10px'})
        ], width=12)
       ]),

       dbc.Row([
            dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph07')
            ], style={'margin-top': '10px', 'margin-left': '10px'})
        ], width=6),
            dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph08')
                ], style={'margin-top': '10px'})
        ], width=6)
    ]),
])



# =========  Callbacks  =========== #
