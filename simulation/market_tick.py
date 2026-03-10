import random

def update_companies(companies):
    """
    Apply a small random weekly change to each company.
    """
    for c in companies:
        # Base random movement (-3% to +3%)
        base_change = random.uniform(-0.03, 0.03)

        change = base_change * c.volatility
        c.market_cap *= (1 + change)

        # Prevent collapse to zero
        c.market_cap = max(c.market_cap, 1.0)


def update_currencies(currencies):
    """
    Apply small random weekly currency movement.
    """
    for cur in currencies:
        if cur.peg_to:
            cur.value = cur.peg_to.value
        else:
            change = random.uniform(-0.01, 0.01)
            cur.update_value(change)