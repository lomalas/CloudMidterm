# main.py

from simulation import countries, currencies
from simulation.live_simulation import run_live_simulation
from simulation.charts import plot_company_history, plot_currency_history, fig_to_base64
from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI()

def flatten_companies(countries):
    all_companies = []
    for country in countries:
        for company in country.companies:
            all_companies.append(company)
    return all_companies

def run_simulation_live():
    """
    Run the live simulation and return a summary of companies and currencies.
    """
    snapshot_manager = run_live_simulation(
        countries,
        currencies,
        weeks=52,
        delay=0  # fast response for API
    )

    all_companies = flatten_companies(countries)
    company_data = [
        {"name": c.name, "market_cap": c.market_cap}
        for c in all_companies[:10]
    ]

    currency_data = [
        {"code": code, "name": curr.name, "value": curr.value}
        for code, curr in currencies.items()
    ]

    return snapshot_manager, company_data, currency_data

# ---------------------------
# FastAPI Endpoints
# ---------------------------
@app.get("/")
def root():
    return {"message": "Hello, Econmy Simulator!"}

@app.get("/simulate")
def simulate():
    snapshot_manager, companies, currencies_data = run_simulation_live()
    result = {
        "message": "Simulation complete",
        "companies": companies,
        "currencies": currencies_data,
        "snapshots_captured": len(snapshot_manager.snapshots)
    }
    return JSONResponse(content=result)

@app.get("/visualize")
def visualize():
    """
    Return HTML with embedded charts for the top company and first currency.
    """
    snapshot_manager, companies, currencies_data = run_simulation_live()

    top_company = companies[0]["name"]
    first_currency = currencies_data[0]["code"]

    company_fig = plot_company_history(snapshot_manager, top_company)
    currency_fig = plot_currency_history(snapshot_manager, first_currency)

    company_img = fig_to_base64(company_fig)
    currency_img = fig_to_base64(currency_fig)

    html_content = f"""
    <html>
        <head><title>Econmy Simulator Charts</title></head>
        <body>
            <h1>Top Company: {top_company}</h1>
            <img src="data:image/png;base64,{company_img}" alt="Company Chart"/>
            <h1>Currency: {first_currency}</h1>
            <img src="data:image/png;base64,{currency_img}" alt="Currency Chart"/>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)