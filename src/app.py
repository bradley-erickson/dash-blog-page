# package imports
import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP
    ],
    title='Sample blog site'
)

def serve_layout():
    return html.Div(
        [
            'Navbar',
            dbc.Container(
                dash.page_container
            )
        ]
    )

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server(debug=True)
