import dash 
from dash import html, dcc, no_update
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc 
from dash import Input, Output, html, no_update
from app import app 
from dash_bootstrap_templates import ThemeSwitchAIO

import plotly.express as px 
import numpy as np 
import pandas as pd 

template_theme1 = "bootstrap"
template_theme2 = "darkly"
url_theme1 = dbc.themes.BOOTSTRAP
url_theme2 = dbc.themes.DARKLY

# ========= Layout ========= #
layout = dbc.Col([ 
    dbc.Card([
        html.H2('Dashboard IBGE', className='title'),
        dbc.Nav([
            dbc.NavLink('Tela principal', className='button title',href='/dados/geral', active='exact', style={'border':'none', 'border-radius':'5px', 'background-color':'#181818', 'color':'white', 'height':'35px', 'font-size':'17px', 'width':'80%', 'text-align':'center', 'margin-left':'10%'}),
            dbc.NavLink('Tela secundária', className='button title', href='/dados/paraiba', active='exact', style={'border':'none', 'border-radius':'5px', 'background-color':'#181818', 'color':'white', 'margin-top':'5px', 'height':'35px', 'font-size':'17px', 'width':'80%', 'text-align':'center', 'margin-left':'10%'}),
            dbc.NavLink('Tela terciária', className='button title', href='/dados/amazonas', active='exact', style={'border':'none', 'border-radius':'5px', 'background-color':'#181818', 'color':'white', 'margin-top':'5px', 'height':'35px', 'font-size':'17px', 'width':'80%', 'text-align':'center', 'margin-left':'10%'}),
        ]),
    ]),
], id='sidebar_completa')