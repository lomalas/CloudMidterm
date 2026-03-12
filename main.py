from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from simulation import countries, currencies
from simulation.charts import plot_company_history, plot_currency_history, fig_to_base64
from simulation.controller import SimulationController
from simulation.snapshot import SnapshotManager

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

# ---------------------------
# FastAPI Endpoints
# ---------------------------

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

@app.get("/status")
def status():
    return controller.status()

@app.get("/company_graph")
def company_graph():
    snapshots = snapshot_manager.get_snapshots()
    if not snapshots:
        return HTMLResponse("<h1>No data yet</h1>")
    top_company = controller.companies[0].name
    fig = plot_company_history(snapshot_manager, top_company)
    img = fig_to_base64(fig)
    return HTMLResponse(f'<img src="data:image/png;base64,{img}" id="company_img"/>')

@app.get("/currency_graph")
def currency_graph():
    snapshots = snapshot_manager.get_snapshots()
    if not snapshots:
        return HTMLResponse("<h1>No data yet</h1>")
    first_currency = list(controller.currencies.keys())[0]
    fig = plot_currency_history(snapshot_manager, first_currency)
    img = fig_to_base64(fig)
    return HTMLResponse(f'<img src="data:image/png;base64,{img}" id="currency_img"/>')

@app.get("/visualize")
def visualize():
    status = controller.status()
    top_company = controller.companies[0].name
    first_currency = list(controller.currencies.keys())[0]

    html_content = f"""
    <html>
        <head>
            <title>Economy Simulator</title>
        </head>
        <body>
            <h1>Economy Simulator</h1>
            <h3>Week: <span id="week">{status['week']}</span></h3>
            <h3>Status: <span id="sim_status">{"RUNNING" if status['running'] else "PAUSED"}</span></h3>
            <h3>Snapshots Stored: <span id="snapshots">{status['snapshots']}</span></h3>

            <div style="margin-bottom:20px">
                <button onclick="play()">▶ Play</button>
                <button onclick="pause()">⏸ Pause</button>
                <button onclick="reset()">🔄 Reset</button>
            </div>

            <h2>Company: {top_company}</h2>
            <img id="company" src="/company_graph"/>

            <h2>Currency: {first_currency}</h2>
            <img id="currency" src="/currency_graph"/>

            <script>
            async function play(){{
                await fetch('/play',{{method:'POST'}});
            }}
            async function pause(){{
                await fetch('/pause',{{method:'POST'}});
            }}
            async function reset(){{
                await fetch('/reset',{{method:'POST'}});
            }}

            // Auto-refresh graphs and status without reloading page
            async function refreshGraphs(){{
                document.getElementById('company').src='/company_graph?'+Date.now();
                document.getElementById('currency').src='/currency_graph?'+Date.now();

                const r = await fetch('/status');
                const data = await r.json();
                document.getElementById('week').innerText = data.week;
                document.getElementById('sim_status').innerText = data.running ? "RUNNING" : "PAUSED";
                document.getElementById('snapshots').innerText = data.snapshots;
            }}

            setInterval(refreshGraphs, 2000); // every 2 seconds
            </script>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content)