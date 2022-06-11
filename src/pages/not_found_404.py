# package imports
import dash
from dash import html

dash.register_page(__name__, path='/404')

layout = html.Div(
    [
        html.H1('404 - Page not found'),
        html.Div(
            html.A('Return home', href='/')
        )
    ]
)
