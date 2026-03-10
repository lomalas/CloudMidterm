import matplotlib.pyplot as plt

def plot_company_history(snapshot_manager, company_name):
    weeks = []
    values = []

    for snap in snapshot_manager.snapshots:
        if company_name in snap.companies:
            weeks.append(snap.week_number)
            values.append(snap.companies[company_name]["market_cap"])

    plt.figure(figsize=(10, 5))
    plt.plot(weeks, values)
    plt.xlabel("Week")
    plt.ylabel("Market Cap")
    plt.title(f"{company_name} – Weekly Market Cap")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_currency_history(snapshot_manager, currency_code):
    weeks = []
    values = []

    for snap in snapshot_manager.snapshots:
        if currency_code in snap.currencies:
            weeks.append(snap.week_number)
            values.append(snap.currencies[currency_code])

    plt.figure(figsize=(10, 5))
    plt.plot(weeks, values)
    plt.xlabel("Week")
    plt.ylabel("Exchange Value")
    plt.title(f"{currency_code} – Weekly Currency Value")
    plt.grid(True)
    plt.tight_layout()
    plt.show()