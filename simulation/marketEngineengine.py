import random

class MarketEngine:
    def __init__(self):
        self.regime = "bull"  # bull, bear, recession
        self.macro_trend = 0.02
        self.volatility_state = 0.01

    def generate_forces(self):
        macro_shock = random.gauss(self.macro_trend, self.volatility_state)

        sector_shocks = {
            "Tech": random.gauss(0, 0.015),
            "Energy": random.gauss(0, 0.)
        }

        return {
            "macro": macro_shock,
            "sectors": sector_shocks
        }