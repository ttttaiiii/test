import dash
from dash import html

dash.register_page(__name__, path = '/page1', name = 'Page 1')

layout = html.Div([
    ## Top row
    html.Div('Top Row: with 1 Col', className = 'block block-top'), ##each row is block and each sides are block-top
    
    ## Middle 2 columns
    html.Div([
        html.Div('Middle Left', className = 'block'), 
        html.Div('Middle Right?', className = 'block')
    ], className = 'row-2'),
    
    ## Footer
    html.Div('Footer', className = 'block block-footer')
], className = 'page1-grid')
