from dash import html, Dash, page_registry, page_container
import dash_bootstrap_components as dbc

app = Dash(__name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

sidebar = html.Div([
    html.Img(src='assets/img/logo.png', className="logo"),
    html.Hr(),
    dbc.Nav([
            dbc.NavLink(
                children=[html.Div(page["name"], className="ms-2")],
                href=page["path"],
                active="exact"
            )
            for page in page_registry.values()
        ],
        vertical=True)
], className='sidebar')

content = html.Div(page_container, className='body')

app.layout = html.Div([sidebar, content])

if __name__ == "__main__":
    app.run(debug=True)
