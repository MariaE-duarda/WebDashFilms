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
                html.Button('Acessar dashboard', className='button-git', id="open2", n_clicks=0),
                dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle("Link do código:", style={'font-weight':'bold'})),
                        dbc.ModalBody("https://github.com/MariaE-duarda/DashTypeWt", style={'font-size':'20px'}),
                        dbc.ModalFooter(
                        dbc.Button(
                                "Fechar", id="close2", className="ms-auto", n_clicks=0, style={'color':'white', 'border-radius':'10px'}
                        )),
                ],
                id="modal2",
                size="lg",
                is_open=False,
                ),
                html.Button('Informações', className='button-git', id="open", n_clicks=0),
                dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle("Informações:", style={'font-weight':'bold'})),
                        dbc.ModalBody("Projeto final da disciplina de Tópicos Especiais de Informática. \nRaspagem de dados e criação de dashboard com os dados extraidos.", style={'font-size':'20px'}),
                        dbc.ModalFooter(
                        dbc.Button(
                                "Fechar", id="close", className="ms-auto", n_clicks=0, style={'color':'white', 'border-radius':'10px'}
                        )),
                ],
                id="modal",
                size="lg",
                is_open=False,
                ),
                html.Button('Site usado',className='button-git', id="open5", n_clicks=0),
                dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle("Link do site usado:", style={'font-weight':'bold'})),
                        dbc.ModalBody("https://m.imdb.com/feature/genre/?ref_=nv_ch_gr", style={'font-size':'20px'}),
                        dbc.ModalFooter(
                        dbc.Button(
                                "Fechar", id="close5", className="ms-auto", n_clicks=0, style={'color':'white', 'border-radius':'10px'}
                        )),
                ],
                id="modal5",
                size="lg",
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
    Output("modal5", "is_open"),
    [Input("open5", "n_clicks"), Input("close5", "n_clicks")],
    [State("modal5", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
