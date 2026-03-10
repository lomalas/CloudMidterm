import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from simulation.market_tick import update_companies, update_currencies


def run_live_simulation(countries, currencies, weeks=52, delay=0.5):
    """
    Runs live updating simulation.
    delay = seconds between ticks
    """

    # Flatten companies
    companies = []
    for country in countries:
        for c in country.companies:
            companies.append(c)

    currency_list = list(currencies.values())

    # Choose companies to display
    tracked_companies = companies[:5]  # first 5 for clarity

    # Data storage
    history = {c.name: [] for c in tracked_companies}
    weeks_data = []

    fig, ax = plt.subplots(figsize=(10, 6))

    def update(frame):
        # Market tick
        update_companies(companies)
        update_currencies(currency_list)

        weeks_data.append(frame)

        for c in tracked_companies:
            history[c.name].append(c.market_cap)

        ax.clear()

        for c in tracked_companies:
            ax.plot(weeks_data, history[c.name], label=c.name)

        ax.set_title("Live Market Simulation")
        ax.set_xlabel("Week")
        ax.set_ylabel("Market Cap")
        ax.legend()
        ax.grid(True)

        time.sleep(delay)

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=range(1, weeks + 1),
        repeat=False
    )

    plt.tight_layout()
    plt.show()