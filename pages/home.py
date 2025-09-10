import dash
from dash import html

dash.register_page(__name__, path = '/home', name = 'Home')

layout = html.Div([
    html.H2('Welcome to my WEBPAGE')
    
])
