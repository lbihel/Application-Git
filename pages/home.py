import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

dash.register_page(__name__, path='/', name='Home')

def layout():
    # Lecture et prétraitement des données
    df = pd.read_csv('database.csv')
    
    # Calculer les KPIs
    total_seismes = len(df)
    avg_magnitude = df['Magnitude'].mean()
    avg_depth = df['Depth'].mean()
    
    # Créer la carte
    fig_map = px.scatter_mapbox(df, 
        lat='Latitude', 
        lon='Longitude',
        color='Magnitude',
        size='Magnitude',
        hover_name='ID',
        hover_data={
            'Date': True,
            'Magnitude': ':.1f',
            'Depth': ':.1f',
            'Latitude': ':.3f',
            'Longitude': ':.3f'
        },
        color_continuous_scale='Viridis',
        zoom=1,
        title='Distribution géographique des séismes'
    )
    
    fig_map.update_layout(
        mapbox_style="open-street-map",
        margin={"r":0,"t":30,"l":0,"b":0},
        height=600
    )
    
    return html.Div([
        # KPIs
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4('Total séismes', className='text-muted'),
                        html.H2(f'{total_seismes:,}'),
                        html.P('Base de données complète')
                    ])
                ], className='shadow-sm')
            ], width=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4('Magnitude moyenne', className='text-muted'),
                        html.H2(f'{avg_magnitude:.1f}'),
                        html.P('Échelle de Richter')
                    ])
                ], className='shadow-sm')
            ], width=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4('Profondeur moyenne', className='text-muted'),
                        html.H2(f'{avg_depth:.0f} km'),
                        html.P('Profondeur des séismes')
                    ])
                ], className='shadow-sm')
            ], width=4),
        ], className='mb-4'),
        
        # Carte
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(
                            id='map-graph',
                            figure=fig_map
                        )
                    ])
                ], className='shadow-sm')
            ])
        ])
    ])