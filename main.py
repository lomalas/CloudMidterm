from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from simulation.controller import SimulationController
from simulation.snapshot import SnapshotManager
from simulation.charts import plot_company_history, plot_currency_history, fig_to_base64
from simulation import countries, currencies

app = FastAPI()

def flatten_companies(countries):
    all_companies = []
    for country in countries:
        for company in country.companies:
            all_companies.append(company)
    return all_companies

all_companies = flatten_companies(countries)
snapshot_manager = SnapshotManager()
controller = SimulationController(all_companies, currencies, snapshot_manager)

@app.get("/")
def root():
    return RedirectResponse("/visualize")

@app.post("/play")
def play():
    controller.play()
    return {"status": "running"}

@app.post("/pause")
def pause():
    controller.pause()
    return {"status": "paused"}

@app.post("/reset")
def reset():
    controller.reset()
    return {"status": "reset"}

@app.get("/debug")
def debug():
    snapshots = snapshot_manager.get_snapshots()
    return {
        "snapshot_count": len(snapshots),
        "week": controller.week,
        "running": controller.running,
        "company_count": len(controller.companies),
        "currency_count": len(controller.currencies),
        "companies": [c.name for c in controller.companies[:3]]
    }

@app.get("/visualize")
def visualize():
    snapshots = controller.snapshot_manager.get_snapshots()

    top_company = controller.companies[0].name
    first_currency = list(controller.currencies.keys())[0]

    company_fig = plot_company_history(controller.snapshot_manager, top_company)
    currency_fig = plot_currency_history(controller.snapshot_manager, first_currency)

    company_img = fig_to_base64(company_fig)
    currency_img = fig_to_base64(currency_fig)

    html_content = f"""
    <html>
        <head>
            <title>Economy Simulator</title>
        </head>
        <body>
            <h1>Economy Simulator</h1>

            <div style="margin-bottom:20px">
                <button onclick="play()">▶ Play</button>
                <button onclick="pause()">⏸ Pause</button>
                <button onclick="reset()">🔄 Reset</button>
            </div>

            <img id="company" src="data:image/png;base64,{company_img}" width="800"/>
            <img id="currency" src="data:image/png;base64,{currency_img}" width="800"/>

            <script>
            function refreshGraphs() {{

             fetch('/company_graph?' + Date.now())
                .then(r => r.json())
                .then(data => {{document.getElementById('company').src = 'data:image/png;base64,' + data.img;}});

            fetch('/currency_graph?' + Date.now())
                .then(r => r.json())
                .then(data => {{document.getElementById('currency').src = 'data:image/png;base64,' + data.img;}});
            }}

            setInterval(refreshGraphs, 2000);

            function play() {{
                fetch('/play', {{method:'POST'}});
            }}
            function pause() {{
                fetch('/pause', {{method:'POST'}});
            }}
            function reset() {{
                fetch('/reset', {{method:'POST'}});
            }}
            </script>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

from fastapi.responses import JSONResponse

@app.get("/company_graph")
def company_graph():
    top_company = controller.companies[0].name
    fig = plot_company_history(controller.snapshot_manager, top_company)
    img = fig_to_base64(fig)
    return JSONResponse({"img": img})

@app.get("/currency_graph")
def currency_graph():
    first_currency = list(controller.currencies.keys())[0]
    fig = plot_currency_history(controller.snapshot_manager, first_currency)
    img = fig_to_base64(fig)
    return JSONResponse({"img": img})