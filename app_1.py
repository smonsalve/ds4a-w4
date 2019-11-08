import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

df = pd.read_csv('aggr.csv', parse_dates=['Entry time'])

app = dash.Dash(__name__)#, external_stylesheets=['https://codepen.io/uditagarwal/pen/oNvwKNP.css', 'https://codepen.io/uditagarwal/pen/YzKbqyV.css'])

app.layout = html.Div(children=[
    html.Div(
            children=[
                html.H2(children="Test", className='h2-title'),
            ],
            className='study-browser-banner row'
    )]
)

if __name__ == "__main__":
    app.run_server(debug=True)
