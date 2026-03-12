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

controller = SimulationController(
    all_companies,
    currencies,
    snapshot_manager
)


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


@app.get("/visualize")
def visualize():

    snapshots = snapshot_manager.get_snapshots()

    status = controller.status()

    if len(snapshots) == 0:

        html = """
        <html>
            <body>
                <h1>Simulation paused. Press Play.</h1>

                <button onclick="play()">▶ Play</button>

                <script>
                function play(){
                    fetch('/play',{method:'POST'})
                    location.reload()
                }
                </script>

            </body>
        </html>
        """

        return HTMLResponse(html)

    top_company = controller.companies[0].name
    first_currency = list(controller.currencies.keys())[0]

    company_fig = plot_company_history(snapshot_manager, top_company)
    currency_fig = plot_currency_history(snapshot_manager, first_currency)

    company_img = fig_to_base64(company_fig)
    currency_img = fig_to_base64(currency_fig)

    html_content = f"""
    <html>
        <head>
            <title>Economy Simulator</title>
            <meta http-equiv="refresh" content="2">
        </head>

        <body>

            <h1>Economy Simulator</h1>

            <h3>Week: {status['week']}</h3>
            <h3>Status: {"RUNNING" if status['running'] else "PAUSED"}</h3>
            <h3>Snapshots Stored: {status['snapshots']}</h3>

            <div style="margin-bottom:20px">

                <button onclick="play()">▶ Play</button>
                <button onclick="pause()">⏸ Pause</button>
                <button onclick="reset()">🔄 Reset</button>

            </div>

            <script>

            function play(){{
                fetch('/play',{{method:'POST'}})
            }}

            function pause(){{
                fetch('/pause',{{method:'POST'}})
            }}

            function reset(){{
                fetch('/reset',{{method:'POST'}})
                location.reload()
            }}

            </script>

            <h2>Company: {top_company}</h2>
            <img src="data:image/png;base64,{company_img}"/>

            <h2>Currency: {first_currency}</h2>
            <img src="data:image/png;base64,{currency_img}"/>

        </body>
    </html>
    """

    return HTMLResponse(content=html_content)