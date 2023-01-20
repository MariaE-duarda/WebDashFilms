from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from dash import dash_table
import plotly.express as px
import plotly.graph_objects as go
from globals import *
from app import app

df = pd.read_csv('1400-filmes.csv')

df = df.sort_values('Nota', ascending=False)
df = df.drop_duplicates(subset='Titulo')

df_ano = df.groupby('Ano').sum().reset_index()
df_nota = df.groupby('Nota').sum().reset_index()
df_votos = df.groupby('Votos').sum().reset_index()

trace = df_nota.groupby('Nota')['Titulo'].sum().tail(10).reset_index()
fig = px.bar(df, x=trace['Nota'].unique(), y=trace['Titulo'].unique())

trace_piores = df_nota.groupby('Nota')['Titulo'].sum().head(10).reset_index()
fig_02 = px.bar(df, x=trace_piores['Nota'].unique(), y=trace_piores['Titulo'].unique())

fig.update_layout(height=280, xaxis={'title': None}, yaxis={'title': None})
fig_02.update_layout(height=280, xaxis={'title': None}, yaxis={'title': None})

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
                    html.Legend('DATASET UTILIZADO', style={'text-align':'center'}),
                    dash_table.DataTable(
                    data=df.to_dict('records'),
                    columns=[{'id': c, 'name': c} for c in df.columns],
                    style_header={ 'border': '1px solid #EAEAEA', 'background-color':'rgba(77, 77, 253, 0.788)', 'color':'white', 'text-align':'center'},
                    filter_action='native',
                    style_cell={ 'border': '1px solid #EAEAEA', 'textAlign': 'left'},
                    page_size=4,     
                    style_data={
                        'whiteSpace': 'normal',
                        'height': 'auto', 'color':'black'
                    }, id='tableData')
                ], style={'margin-top': '15px', 'margin-left': '10px'}),
        ], width=12),
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
                    dbc.Tabs([
                        dcc.Tab(label='Melhores Avaliações', children=[
                            dcc.Graph(id='graph2', className='dbc', config={"displayModeBar": False, "showTips": False}, figure=fig),
                            dbc.Button("Abrir modal", id="open2", n_clicks=0, style={'border':'none', 'border-radius':'5px', 'width':'95%', 'margin-left':'10px', 'margin-top':'5px', 'margin-bottom':'10px'}),
                            dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Melhores Avaliações:")),
                                dbc.ModalBody(dcc.Graph(id='graph02', className='dbc', config={"displayModeBar": False, "showTips": False}, figure=fig)),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Fechar", id="close2", className="ms-auto", n_clicks=0, style={'border-radius':'5px'}
                                    )
                                ),
                            ],
                            id="modal2",
                            size="xl",
                            is_open=False,
                        ),
                        ], style={'color':'white', 'background-color':'#181D3135'}),
                        dcc.Tab(label='Piores Avaliações', children=[
                            dcc.Graph(id='graph5', className='dbc', config={"displayModeBar": False, "showTips": False}, animate=True, figure=fig_02),
                            dbc.Button("Abrir modal", id="open3", n_clicks=0, style={'border':'none', 'border-radius':'5px', 'width':'95%', 'margin-left':'10px', 'margin-top':'5px', 'margin-bottom':'10px'}),
                        ]),
                        dbc.Modal([
                            dbc.ModalHeader(dbc.ModalTitle("Piores Avaliações:")),
                            dbc.ModalBody(dcc.Graph(id='graph05', className='dbc', config={"displayModeBar": False, "showTips": False}, figure=fig_02)),
                            dbc.ModalFooter(
                                dbc.Button(
                                    "Fechar", id="close3", className="ms-auto", n_clicks=0, style={'border-radius':'5px'}
                                )
                            ),
                        ],
                        id="modal3",
                        size="xl",
                        is_open=False,
                    ),
                    ], style={'color':'white', 'background-color':'#181D3135'})
                ], style={'margin-top': '10px', 'margin-left':'10px'})
        ], width=9),
        dbc.Col([
            dbc.Card([
                dcc.Graph(id='graph')
            ], style={'margin-top': '10px'})
        ], width=3)
    ]),
])



# =========  Callbacks  =========== #
@app.callback(
    Output("modal2", "is_open"),
    [Input("open2", "n_clicks"), Input("close2", "n_clicks")],
    [State("modal2", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal3", "is_open"),
    [Input("open3", "n_clicks"), Input("close3", "n_clicks")],
    [State("modal3", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open