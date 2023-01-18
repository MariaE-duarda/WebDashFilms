from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar
from globals import *
from app import app


df = pd.read_csv('vgsales.csv')

df_NA_Sales = df.groupby('NA_Sales').sum().reset_index()
df_EU_Sales = df.groupby('EU_Sales').sum().reset_index()
df_JP_Sales = df.groupby('NA_Sales').sum().reset_index()

df_year = df.groupby('Year').sum().reset_index()
df_name = df.groupby('Name').sum().reset_index()
sort_name = df_name.value_counts('Name').head(5)
df_plaforma = df.groupby('Platform').sum().reset_index().head(8)
df_genero = df.groupby('Genre').sum().reset_index().head(5)

top_name = df.groupby(['Publisher'])['Global_Sales'].sum()
top_name = top_name.sort_values(ascending=True).head(10).reset_index()

genero_fig_pizza = px.pie(
        df_genero, values='Global_Sales', 
        names='Genre', hole=.3)

publicados_fig_pizza = px.pie(
    df_plaforma, values='Global_Sales', 
    names='Platform', hole=.3
)

name_fig = px.bar(top_name, x='Publisher', y='Global_Sales')

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
            dbc.CardGroup([
                dbc.Card([
                    html.Legend('Venda geral na América do Norte:'),
                    html.H6(round(df['NA_Sales'].sum()))
                    # dcc.Input(value=round(df['NA_Sales'].sum()), style={'border':'none'}),
                ], style={'padding-left':'20px', 'padding-top':'10px'}),
                dbc.Card(
                    html.Div(className='fa fa-gamepad', style= card_icon),
                    color="yellow",
                    style={'maxWidth': 75, 'height':100, 'margin-left':'-10px'},
                )
            ])
        ], width=4),
                dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend('Venda geral na Europa:'),
                    html.H6(round(df['EU_Sales'].sum())),
                ], style={'padding-left':'20px', 'padding-top':'10px'}),
                dbc.Card(
                    html.Div(className='fa fa-gamepad', style= card_icon),
                    color="green",
                    style={'maxWidth': 75, 'height':100, 'margin-left':'-10px'},
                )
            ])
        ], width=4),
                dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend('Venda geral no Japão:'),
                    html.H6(round(df['JP_Sales'].sum())),
                ], style={'padding-left':'20px', 'padding-top':'10px'}),
                dbc.Card(
                    html.Div(className='fa fa-gamepad', style= card_icon),
                    color="blue",
                    style={'maxWidth': 75, 'height':100, 'margin-left':'-10px'},
                )
            ])
        ], width=4),
       ], style={'margin':'10px'}), 

       dbc.Row([
            dbc.Col([
                dbc.Col([
                    html.Label('Filtrar jogos: ', className='card-title', style={'font-size':'23px'}),
                    html.Br(),
                    html.Label('Plataformas: '),
                    html.Div(
                        dcc.Dropdown(
                            id='dropdown-plataforma', 
                            clearable=False,
                            style={'width':'100%'},
                            persistence=True,
                            persistence_type="session", 
                            multi=True, options=[{"label":x, "value":x} for x in df['Platform'].unique()], 
                            value=df['Platform'].unique()
                        ) 
                    ),
                    html.Label('Gêneros: '),
                        dcc.Dropdown(
                            id='dropdown-generos', 
                            clearable=False,
                            style={'width':'100%'},
                            persistence=True,
                            persistence_type="session", 
                            multi=True, options=[{"label":x, "value":x} for x in df['Genre'].unique()], 
                            value=df['Genre'].unique()
                    ),
                ], style={'padding':'10px'})
            ], width=4, style={'border': '1px solid #c6c6c6'}),
                dbc.Col([
                    dbc.Card([
                        html.H4('Número de vendas:', style={'text-align':'center', 'margin-botton':'-50px', 'margin-top': '20px'}),
                        dcc.Graph(figure=name_fig, id="name_fig", style={'height': 350}),
                    ], style={'margin-left':'15px'})
                ], width=8)
       ], style={'margin': '10px'}),
       dbc.Row([
            dbc.Col(dbc.Card([
                html.H4('Top 5 vendas por genêro:', style={'margin':'20px'}),
                dcc.Graph(figure=genero_fig_pizza, id='genero_fig_pizza', style={'height': 380})]), width=6, style={'margin-left':'10px'}),
            dbc.Col(dbc.Card([
                html.H4('Top 8 vendas por plataforma:', style={'margin':'20px'}),
                dcc.Graph(figure=publicados_fig_pizza, id='publicados_fig_pizza',style={'width':'800px', 'padding':'-20px','height': 380})])),
       ])
])



# =========  Callbacks  =========== #
@app.callback([
    Output('name_fig', 'figure'),
    Output('genero_fig_pizza', 'figure'),
    Output('publicados_fig_pizza', 'figure'),
    ],[
    Input('dropdown-plataforma', 'value'),
    Input('dropdown-generos', 'value'),
])
def atualizar_graficos(plataforma, genero):
    df_geral = df[(df["Platform"].isin(plataforma)) & df['Genre'].isin(genero)]

    plataform = df_geral.groupby('Platform').sum().reset_index().head(8)
    genre = df_geral.groupby('Genre').sum().reset_index().head(5)

    name = df_geral.groupby(['Publisher'])['Global_Sales'].sum()
    name = name.sort_values(ascending=False).head(10).reset_index()

    genero_fig_pizza = px.pie(
        genre, values='Global_Sales', 
        names='Genre', hole=.3)

    publicados_fig_pizza = px.pie(
        plataform, values='Global_Sales', 
        names='Platform', hole=.3
    )
    name_fig = px.bar(name, x='Publisher', y='Global_Sales')

    return name_fig, genero_fig_pizza, publicados_fig_pizza

