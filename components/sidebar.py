import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd

# ========= Layout ========= #
layout = dbc.Col([
        dbc.Card([
                html.H1('Lista de Filmes', className='text-primary'),
                html.P('Tópicos Especiais de Informática', className='text-info'),
                html.Hr(),

        #Seção perfil
                dbc.Button(id='botao_avatar',
                children=[html.Img(src='/assets/filme.png', id='avatar_change', alt='Avatar', className='perfil_avatar')], 
                style={'background-color':'transparent', 'border-color':'transparent'}),
                html.Button('Acessar dashboard', className='button-git'),
                html.Button('Informações', className='button-git', id="open", n_clicks=0),
                dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle("Informações")),
                        dbc.ModalBody("Projeto final de Tópicos de informática"),
                        dbc.ModalFooter(
                        dbc.Button(
                                "Fechar", id="close", className="ms-auto", n_clicks=0, style={'color':'black'}
                        )),
                ],
                id="modal",
                #size="lg",
                is_open=False,
                ),
        ], id='sidebar_completa', style={'margin-top':'15px', 'text-align':'center'}),
        ])





# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
