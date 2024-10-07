from turtle import color
import dash
from dash import html
import pandas as pd
import numpy as np
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
from dash import dash_table
 
from model import *

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(children='Rock vs Hip-Hop', style={'color': 'red'}),
    html.Div([
        'Acousticness: ',
        dcc.Input(id='acousticnessValue', type='text'),
        html.Br(),
        'Danceability: ',
        dcc.Input(id='danceabilityValue', type='text'),
        html.Br(),
        'Energy: ',
        dcc.Input(id='energyValue', type='text'),
        html.Br(),
        'Instrumentalness: ',
        dcc.Input(id='instrumentalnessValue', type='text'),
        html.Br(),
        'Liveness: ',
        dcc.Input(id='livenessValue', type='text'),
        html.Br(),
        'Speechiness: ',
        dcc.Input(id='speechinessValue', type='text'),
        html.Br(),
        'Tempo: ',
        dcc.Input(id='tempoValue', type='text'),
        html.Br(),
        'Valence: ',
        dcc.Input(id='valenceValue', type='text')]),
        
        html.Br(),
        html.Hr(),
        html.Div(id='outputDiv')

    ])

@app.callback(
    Output(component_id='outputDiv', component_property='children'),
    Input(component_id='acousticnessValue', component_property='value'),
    Input(component_id='danceabilityValue', component_property='value'),
    Input(component_id='energyValue', component_property='value'),
    Input(component_id='instrumentalnessValue', component_property='value'),
    Input(component_id='livenessValue', component_property='value'),
    Input(component_id='speechinessValue', component_property='value'),
    Input(component_id='tempoValue', component_property='value'),
    Input(component_id='valenceValue', component_property='value')
)

def update_output_div(acousticness, danceability, energy, instrumentalness, liveness, speechiness, tempo, valence):
    random_forest = get_model()
    # cast from text to float
    acousticness = float(acousticness)
    danceability = float(danceability)
    energy = float(energy)
    instrumentalness = float(instrumentalness)
    liveness = float(liveness)
    speechiness = float(speechiness)
    tempo = float(tempo)
    valence = float(valence)
    forecastValue = random_forest.predict([[acousticness, danceability, energy, instrumentalness, liveness, speechiness, tempo, valence]])
    message = 'The genre is: ' + forecastValue[0] 
    return message

if __name__ == '__main__':
    app.run_server(debug=True)
