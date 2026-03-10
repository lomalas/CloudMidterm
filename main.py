# main.py

from simulation import countries, currencies
from simulation.live_simulation import run_live_simulation
from simulation.run_simulation import *
from simulation.charts import (
    plot_company_history,
    plot_currency_history
)


def flatten_companies(countries):
    """
    Convert country -> companies structure
    into a single list of companies.
    """
    all_companies = []
    for country in countries:
        for company in country.companies:
            all_companies.append(company)
    return all_companies



def main():
    print("=== ECONOMY SIMULATION START ===")

    # ---------------------------
    # CONFIG
    # ---------------------------
    WEEKS_TO_SIMULATE = 26  # 6 months
    SNAPSHOT_DIR = "snapshots"

    # ---------------------------
    # RUN SIMULATION
    # ---------------------------
    '''
    snapshot_manager = run_simulation(
        weeks=WEEKS_TO_SIMULATE,
        countries=countries,
        currencies=currencies,
        snapshot_dir=SNAPSHOT_DIR
    )
    '''
    snapshot_manager = run_live_simulation(
    countries,
    currencies,
    weeks=52,
    delay=0.5   # half second between ticks
    )

    print(f"\nSimulation complete.")
    print(f"Snapshots captured: {len(snapshot_manager.snapshots)}")

    # ---------------------------
    # PRINT FINAL STATE SUMMARY
    # ---------------------------
    all_companies = flatten_companies(countries)

    print("\nFinal Company Market Caps:")
    for company in all_companies[:10]:  # limit output
        print(f"{company.name}: ${company.market_cap:.2f}")

    print("\nFinal Currency Values:")
    for code, currency in currencies.items():
        print(f"{currency.name} ({code}): {currency.value:.4f}")

    # ---------------------------
    # PLOT EXAMPLES
    # ---------------------------
    # Change these names if needed
    example_company = all_companies[0].name
    example_currency = list(currencies.keys())[0]

    print(f"\nPlotting {example_company} history...")
    plot_company_history(snapshot_manager, example_company)

    print(f"\nPlotting {example_currency} currency history...")
    plot_currency_history(snapshot_manager, example_currency)

    print("=== END ===")


if __name__ == "__main__":
    main()