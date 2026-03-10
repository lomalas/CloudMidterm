import dash
from dash import dcc, html
from dash.dependencies import Output, Input, State
import plotly.graph_objs as go
import random

app = dash.Dash(__name__)
server = app.server

# Shared state
weeks = []
company_data = {"TechCorp": [100], "OilCo": [100]}
currency_data = {"USD": [1.0], "EUR": [1.0]}
week_index = 0

app.layout = html.Div([

    html.H1("Live Market Simulation"),

    # Page Toggle Buttons
    html.Div([
        html.Button("Stocks View", id="stocks-view-btn"),
        html.Button("Currencies View", id="currencies-view-btn"),
    ]),

    dcc.Store(id="view-mode", data="stocks"),
    dcc.Store(id="running", data=True),

    dcc.Graph(id="live-chart"),

    dcc.Interval(id="interval", interval=500),

    html.Button("Pause", id="pause-btn"),
    html.Button("Play", id="play-btn"),

    html.Hr(),

    html.H3("Add Company"),
    dcc.Input(id="company-name", type="text", placeholder="Company Name"),
    dcc.Input(id="company-start", type="number", value=100),
    html.Button("Add Company", id="add-company-btn"),

    html.Hr(),

    html.H3("Add Currency"),
    dcc.Input(id="currency-name", type="text", placeholder="Currency Name"),
    dcc.Input(id="currency-start", type="number", value=1.0),
    html.Button("Add Currency", id="add-currency-btn"),
])


# Toggle Stocks/Currencies Page
@app.callback(
    Output("view-mode", "data"),
    Input("stocks-view-btn", "n_clicks"),
    Input("currencies-view-btn", "n_clicks"),
    prevent_initial_call=True
)
def switch_view(stocks, currencies):
    ctx = dash.callback_context.triggered[0]["prop_id"]
    return "stocks" if "stocks-view-btn" in ctx else "currencies"


# Play / Pause
@app.callback(
    Output("running", "data"),
    Input("play-btn", "n_clicks"),
    Input("pause-btn", "n_clicks"),
    prevent_initial_call=True
)
def toggle_play(play, pause):
    ctx = dash.callback_context.triggered[0]["prop_id"]
    return True if "play-btn" in ctx else False


# Add Company (starts at CURRENT week)
@app.callback(
    Output("company-name", "value"),
    Input("add-company-btn", "n_clicks"),
    State("company-name", "value"),
    State("company-start", "value"),
    prevent_initial_call=True
)
def add_company(n, name, start_value):
    if name and name not in company_data:
        # Pad history so it starts at current week
        padded_history = [None] * len(weeks)
        padded_history.append(start_value)
        company_data[name] = padded_history
    return ""


# Add Currency (starts at CURRENT week)
@app.callback(
    Output("currency-name", "value"),
    Input("add-currency-btn", "n_clicks"),
    State("currency-name", "value"),
    State("currency-start", "value"),
    prevent_initial_call=True
)
def add_currency(n, name, start_value):
    if name and name not in currency_data:
        padded_history = [None] * len(weeks)
        padded_history.append(start_value)
        currency_data[name] = padded_history
    return ""


# Main Update Loop
@app.callback(
    Output("live-chart", "figure"),
    Input("interval", "n_intervals"),
    Input("running", "data"),
    Input("view-mode", "data")
)
def update_graph(n, running, view_mode):
    global week_index

    if running:
        week_index += 1
        weeks.append(week_index)

        # Update companies
        for name in company_data:
            last = next((v for v in reversed(company_data[name]) if v is not None), 100)
            company_data[name].append(last * (1 + random.uniform(-0.03, 0.03)))

        # Update currencies
        for name in currency_data:
            last = next((v for v in reversed(currency_data[name]) if v is not None), 1.0)
            currency_data[name].append(last * (1 + random.uniform(-0.01, 0.01)))

    fig = go.Figure()

    if view_mode == "stocks":
        for name, vals in company_data.items():
            fig.add_trace(go.Scatter(
                x=weeks,
                y=vals,
                mode="lines",
                name=name
            ))
    else:
        for name, vals in currency_data.items():
            fig.add_trace(go.Scatter(
                x=weeks,
                y=vals,
                mode="lines",
                name=name
            ))

    fig.update_layout(
        xaxis_title="Week",
        yaxis_title="Value",
        template="plotly_dark"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)