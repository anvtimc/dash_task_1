import dash_bootstrap_components as dbc
from dash import dcc

def create_layout():
    return dbc.Container([
        dbc.NavbarSimple(
            brand="Качество воздуха 🏗️🏙️",
            brand_href="#",
            brand_style={"fontSize": "32px", "fontWeight": "semibold"},
            className="mb-3"
        ),

        dbc.Row([
            dbc.Col([
                dbc.Card(id='city-card', body=True),
            ], width=6, md=6, xs=12),
            dbc.Col([
                dbc.Input(id='city-input', value='Moscow', placeholder="Введите город", type='text', debounce=True, style={'fontSize': '20px', 'fontWeight': 'bold'}),
            ], width=6, md=6, xs=12),
        ], className="mb-3"),

        dbc.Row([
            dbc.Col(dcc.Graph(id='co-graph'), width=6, md=4, xs=12),
            dbc.Col(dcc.Graph(id='no2-graph'), width=6, md=4, xs=12),
            dbc.Col(dcc.Graph(id='o3-graph'), width=6, md=4, xs=12),
        ], className="mb-3"),

        dbc.Row([
            dbc.Col(dcc.Graph(id='so2-graph'), width=6, md=4, xs=12),
            dbc.Col(dcc.Graph(id='pm25-graph'), width=6, md=4, xs=12),
            dbc.Col(dcc.Graph(id='pm10-graph'), width=6, md=4, xs=12),
        ], className="mb-3"),

    ], fluid=True)
