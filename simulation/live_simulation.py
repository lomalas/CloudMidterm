from simulation.market_tick import update_companies, update_currencies
from simulation.snapshot import SnapshotManager
import time


def run_live_simulation(countries, currencies, snapshot_manager, delay=1):

    # Flatten companies
    companies = []
    for country in countries:
        for c in country.companies:
            c.country = country
            companies.append(c)

    currency_list = list(currencies.values())

    week = 1

    while True:

        update_companies(companies)
        update_currencies(currency_list)

        snapshot_manager.capture_week(
            week,
            companies,
            currency_list
        )

        week += 1

        time.sleep(delay)