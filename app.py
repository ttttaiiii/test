from dash import Dash, dcc, html, page_container
import dash_bootstrap_components as dbc

## Initialize the app
app = Dash(__name__, use_pages = True, suppress_callback_exceptions = True,
           title = 'Tai Multi-Page App')
server = app.server ## for deployment

app.layout = html.Div([
    dbc.NavbarSimple(
        children = [
            dbc.NavLink('Home', href = '/home', active = 'exact'),
            dbc.NavLink('Page 1', href = '/page1', active = 'exact'),
            dbc.NavLink('Cat Fact', href = '/page2', active = 'exact'),
            dbc.NavLink('Page 3', href = '/page3', active = 'exact')
            
        ],
        brand = 'Tai Chi'
    ),
    page_container
])

# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)