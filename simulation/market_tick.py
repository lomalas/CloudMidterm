import random

def update_companies(companies):
    """
    Apply a small random weekly change to each company.
    """
    for c in companies:
        # Base random movement (-3% to +3%)
        base_change = random.uniform(-0.03, 0.03)
        change = base_change * getattr(c, "volatility", 1.0)
        c.market_cap *= (1 + change)

        # Prevent collapse to zero
        c.market_cap = max(c.market_cap, 1.0)


def update_currencies(currencies):
    """
    Apply small random weekly currency movement.
    Accepts a list of currency objects.
    """
    for cur in currencies:
        if getattr(cur, "peg_to", None):
            # If pegged, copy value from the pegged currency
            cur.value = cur.peg_to.value
        else:
            # Random small fluctuation
            change = random.uniform(-0.01, 0.01)
            # Use update_value() if it exists, else direct assignment
            if hasattr(cur, "update_value"):
                cur.update_value(change)
            else:
                cur.value *= (1 + change)