import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import io
import base64

def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img_bytes = buf.read()
    buf.close()
    plt.close(fig)
    return base64.b64encode(img_bytes).decode('utf-8')


def _get_scale(values):
    """Return (divisor, unit_label) based on the magnitude of values."""
    max_val = max(values) if values else 1
    if max_val >= 1_000_000_000_000:
        return 1_000_000_000_000, "Trillions (USD)"
    elif max_val >= 1_000_000_000:
        return 1_000_000_000, "Billions (USD)"
    elif max_val >= 1_000_000:
        return 1_000_000, "Millions (USD)"
    else:
        return 1, "USD"


def plot_company_history(snapshot_manager, company_name):
    snapshots = snapshot_manager.get_snapshots()
    if not snapshots:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.text(0.5, 0.5, "No data yet", ha='center', va='center', fontsize=14)
        return fig

    weeks = []
    values = []
    for snap in snapshots:
        weeks.append(snap.week_number)
        val = snap.companies.get(company_name, {}).get("market_cap", 0)
        values.append(val)

    divisor, unit_label = _get_scale(values)
    scaled = [v / divisor for v in values]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(weeks, scaled, marker="o", linewidth=2, color="steelblue")
    ax.set_xlabel("Week")
    ax.set_ylabel(f"Market Cap ({unit_label})")
    ax.set_title(f"{company_name} – Weekly Market Cap")
    ax.grid(True, alpha=0.4)

    # Tight y-axis: pad 10% above and below the actual data range
    lo, hi = min(scaled), max(scaled)
    pad = (hi - lo) * 0.10 if hi != lo else hi * 0.05
    ax.set_ylim(lo - pad, hi + pad)

    # Clean tick formatting (e.g. 1.23 not 1.2300000001)
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.2f'))

    fig.tight_layout()
    return fig


def plot_currency_history(snapshot_manager, currency_code):
    snapshots = snapshot_manager.get_snapshots()
    if not snapshots:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.text(0.5, 0.5, "No data yet", ha='center', va='center', fontsize=14)
        return fig

    weeks = []
    values = []
    for snap in snapshots:
        weeks.append(snap.week_number)
        val = snap.currencies.get(currency_code, 0)
        values.append(val)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(weeks, values, marker="o", linewidth=2, color="seagreen")
    ax.set_xlabel("Week")
    ax.set_ylabel("Exchange Rate (vs USD)")
    ax.set_title(f"{currency_code} – Weekly Exchange Rate")
    ax.grid(True, alpha=0.4)

    # Tight y-axis
    lo, hi = min(values), max(values)
    pad = (hi - lo) * 0.10 if hi != lo else hi * 0.05
    ax.set_ylim(lo - pad, hi + pad)

    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.4f'))

    fig.tight_layout()
    return fig