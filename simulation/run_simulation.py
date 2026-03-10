from simulation.market_tick import update_companies, update_currencies
from simulation.snapshot import SnapshotManager
import time


def run_live_simulation(
    countries,
    currencies,
    weeks=52,
    delay=0.5,
    snapshot_dir="snapshots"
):
    snapshot_manager = SnapshotManager(snapshot_dir)

    # Flatten companies
    all_companies = []
    for country in countries:
        for c in country.companies:
            c.country = country
            all_companies.append(c)

    currency_list = list(currencies.values())

    for week in range(1, weeks + 1):
        update_companies(all_companies)
        update_currencies(currency_list)

        snapshot_manager.capture_week(
            week,
            all_companies,
            currency_list
        )

        time.sleep(delay)

    return snapshot_manager  # ← THIS IS WHAT YOU’RE MISSING