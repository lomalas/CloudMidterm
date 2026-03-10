import streamlit as st
import plotly.graph_objects as go
import random
import time

st.set_page_config(layout="wide")

# -----------------------
# SESSION STATE
# -----------------------

if "running" not in st.session_state:
    st.session_state.running = False

if "week" not in st.session_state:
    st.session_state.week = 0

if "stocks" not in st.session_state:
    st.session_state.stocks = {
        "TechCorp": [100],
        "OilCo": [100],
    }

if "currencies" not in st.session_state:
    st.session_state.currencies = {
        "USD": [1.0],
        "EUR": [1.0],
    }

# -----------------------
# SIDEBAR CONTROLS
# -----------------------

st.sidebar.title("Simulation Controls")

col1, col2 = st.sidebar.columns(2)

with col1:
    if st.button("▶ Play"):
        st.session_state.running = True

with col2:
    if st.button("⏸ Pause"):
        st.session_state.running = False

speed = st.sidebar.slider("Seconds per tick", 0.1, 2.0, 0.5)

chart_type = st.sidebar.selectbox("Chart Type", ["Stocks", "Currencies"])

# -----------------------
# ADD OBJECTS
# -----------------------

st.sidebar.markdown("---")

company_name = st.sidebar.text_input("New Company Name")
if st.sidebar.button("Add Company"):
    if company_name and company_name not in st.session_state.stocks:
        st.session_state.stocks[company_name] = (
            [None] * st.session_state.week + [100]
        )

currency_name = st.sidebar.text_input("New Currency Code")
if st.sidebar.button("Add Currency"):
    if currency_name and currency_name not in st.session_state.currencies:
        st.session_state.currencies[currency_name] = (
            [None] * st.session_state.week + [1.0]
        )

# -----------------------
# TICK FUNCTION
# -----------------------

def tick():
    st.session_state.week += 1

    for name, values in st.session_state.stocks.items():
        last = next((v for v in reversed(values) if v is not None), 100)
        values.append(last * (1 + random.uniform(-0.03, 0.03)))

    for name, values in st.session_state.currencies.items():
        last = next((v for v in reversed(values) if v is not None), 1.0)
        values.append(last * (1 + random.uniform(-0.01, 0.01)))

# -----------------------
# LIVE FRAGMENT
# -----------------------

@st.fragment(run_every="500ms")
def live_chart():

    if st.session_state.running:
        tick()

    fig = go.Figure()

    data_source = (
        st.session_state.stocks
        if chart_type == "Stocks"
        else st.session_state.currencies
    )

    for name, values in data_source.items():
        fig.add_trace(
            go.Scatter(
                y=values,
                mode="lines",
                name=name
            )
        )

    fig.update_layout(
        title=f"{chart_type} - Week {st.session_state.week}",
        height=600
    )

    st.plotly_chart(fig, width="stretch")


live_chart()