from utils.data_loader import load_data
import plotly.graph_objects as go
from dash import Input, Output, html


def register_callbacks(app):

    @app.callback(
        Output('city-card', 'children'),
        Output('co-graph', 'figure'),
        Output('no2-graph', 'figure'),
        Output('o3-graph', 'figure'),
        Output('so2-graph', 'figure'),
        Output('pm25-graph', 'figure'),
        Output('pm10-graph', 'figure'),
        Input('city-input', 'value')
    )
    def update_dashboard(city):
        data = load_data(city)

        co_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['co_hours'], mode='lines+markers')],
            layout=go.Layout(title="Содержание CO в воздухе", 
                           xaxis_title='Время суток', 
                           yaxis_title='Индекцс по CO',
                           template='plotly_white')
        )

        no2_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['no2_hours'], mode='lines+markers')],
            layout=go.Layout(title="Содержание NO₂ в воздухе", 
                           xaxis_title='Время суток', 
                           yaxis_title='Индекцс по NO₂',
                           template='plotly_white')
        )

        o3_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['o3_hours'], mode='lines+markers')],
            layout=go.Layout(title="Содержание O₃ в воздухе", 
                           xaxis_title='Время суток', 
                           yaxis_title='Индекцс по O₃',
                           template='plotly_white')
        )

        so2_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['so2_hours'], mode='lines+markers')],
            layout=go.Layout(title="Содержание SO₂ в воздухе", 
                           xaxis_title='Время суток', 
                           yaxis_title='Индекцс по SO₂',
                           template='plotly_white')
        )

        pm25_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['pm25_hours'], mode='lines+markers')],
            layout=go.Layout(title="Содержание частиц размером <2.5 мкм", 
                           xaxis_title='Время суток', 
                           yaxis_title='Индекцс по частицам',
                           template='plotly_white')
        )

        pm10_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['pm10_hours'], mode='lines+markers')],
            layout=go.Layout(title="Содержание частиц размером <1.0 мкм", 
                           xaxis_title='Время суток', 
                           yaxis_title='Индекцс по частицам',
                           template='plotly_white')
        )

        city_card = html.Div([
            html.H4("Текущие показатели"),
            html.P(f"Температура: {data['temp']} °C"),
            html.P(f"{data['last_updated']}"),
            html.P(f"{data['condition']}"),
            html.Img(src=f"https:{data['icon']}")
            ])

        return city_card, co_fig, no2_fig, o3_fig, so2_fig, pm25_fig, pm10_fig
