# package imports
import dash
from dash import html
import dash_bootstrap_components as dbc

# local imports
from .blog.layout import article_cards

dash.register_page(
    __name__,
    path='/',
    redirect_from=['/home'],
    title='Sample blog'
)


# show the 3 most recent blog posts
blog = [
    dbc.Col(
        item,
        md=6,
        align='stretch'
    ) for item in article_cards[:3]
]

layout = html.Div(
    [
        html.H2('Home page!'),
        html.A(
            'Click here to go to the blog section!',
            href='/blog'
        ),
        html.H4('Recent Posts'),
        dbc.Row(
            blog,
            class_name='g-3'
        )
    ]
)
