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
                html.P('By Tópicos Especiais de Info', className='text-info'),
                html.Hr(),

        #Seção perfil
                dbc.Button(id='botao_avatar',
                children=[html.Img(src='/assets/Game-Icon.png', id='avatar_change', alt='Avatar', className='perfil_avatar')], 
                style={'background-color':'transparent', 'border-color':'transparent'}),
                html.Button('Acessar dashboard', className='button-git', style={'margin-left':'15%'}),
        ], id='sidebar_completa', style={'margin-top':'10px', 'text-align':'center'}),
        ])





# =========  Callbacks  =========== #
# Pop-up receita
