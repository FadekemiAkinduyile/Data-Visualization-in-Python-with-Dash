import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

import streamlit as st
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from streamlit_dash import st_id_selector
import sys

#Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")

#Create a plotly figure for use by dcc.Graph()
fig = px.line(
    data,
    title="Precious Metal Prices 2018-2021",
    x="DateTime",
    y=["Gold"],
    color_discrete_map={"Gold": "gold"}
)

app = dash.Dash(__name__)
app.title = "Precious Metal Prices 2018-2021"
server = app.server

app.layout = html.Div(
    id="app-container",
    children=[
        html.Div(
            id="header-area",
            children=[
                html.H1(
                    id="header-title",
                    children="Gold Prices",
                ),
                html.P(
                    id="header-description",
                    children=("The cost of precious metals", html.Br(), "between 2018 and 2021"),
                ),
            ],
        ),
        html.Div(
            id="menu-area",
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className="menu-title",
                            children="Metal"
                        ),
                        dcc.Dropdown(
                            id="metal-filter",
                            className="dropdown",
                            options=[{"label": metal, "value":metal} for metal in data.columns[1:]],
                            clearable=False,
                            value="Gold"
                        )
                    ]
                )
            ]
        ),
        html.Div(
            id="graph-container",
            children=dcc.Graph(
                id="price-chart",
                figure=fig,
                config={"displayModeBar": False}
            ),
        ),
    ]
)

@app.callback(
    Output("price-chart", "figure"),
    Input("metal-filter", "value")
)
def update_chart(metal):
    # Create a plotly figure for use by dcc.Graph()
    fig = px.line(
        data,
        title="Precious Metal Prices 2018-2021",
        x="DateTime",
        y=[metal],
        color_discrete_map={
            "Platinum": "#E5E4E2G",
            "Gold": "gold",
            "Silver": "silver",
            "Palladium": "#CED0DD",
            "Rhodium": "#E2E7E1",
            "Iridium": "#3D3C3A",
            "Ruthenium": "#C9CBC8"
        }
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Date",
        yaxis_title="Price (USD/oz)",
        font=dict(
            family="Verdana, sans-serif",
            size=18,
            color="white"
        ),
    )

    return fig

if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
    except IndexError:
        port = 8050  # Default port if not specified in command line arguments

    app.run_server(debug=True, use_reloader=False, port=port)
