import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


def plot_company_history(snapshot_manager, company_name):

    weeks = []
    values = []

    for snap in snapshot_manager.snapshots:

        weeks.append(snap.week)

        company_value = None

        for company in snap.companies:
            if company.name == company_name:
                company_value = company.market_cap
                break

        if company_value is not None:
            values.append(company_value)
        else:
            values.append(0)

    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(weeks, values, marker="o")

    ax.set_xlabel("Week")
    ax.set_ylabel("Market Cap")
    ax.set_title(f"{company_name} – Weekly Market Cap")

    ax.grid(True)

    return fig


def plot_currency_history(snapshot_manager, currency_code):

    weeks = []
    values = []

    for snap in snapshot_manager.snapshots:

        weeks.append(snap.week)

        currency_value = None

        for currency in snap.currencies:
            if currency.code == currency_code:
                currency_value = currency.value
                break

        if currency_value is not None:
            values.append(currency_value)
        else:
            values.append(0)

    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(weeks, values, marker="o")

    ax.set_xlabel("Week")
    ax.set_ylabel("Currency Value")
    ax.set_title(f"{currency_code} – Weekly Currency Value")

    ax.grid(True)

    return fig