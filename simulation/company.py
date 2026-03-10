import random

class Company:
    def __init__(
        self,
        name,
        country,
        sector,
        market_cap,
        volatility,
        growth_rate,
        debt_ratio,
        dependencies=None
    ):
        self.name = name
        self.country = country              # Should eventually be Country object
        self.sector = sector

        # Core Financials
        self.market_cap = market_cap        # Current valuation
        self.volatility = volatility        # 0.0 - 1.0 (reaction intensity)
        self.growth_rate = growth_rate      # Baseline annual growth %
        self.debt_ratio = debt_ratio        # 0.0 - 1.0 (risk exposure)

        # Economic Links
        self.dependencies = dependencies if dependencies else []

    # -----------------------------------
    # Market Behavior Methods
    # -----------------------------------

    def apply_market_change(self, percent_change):
        """
        Applies a percentage change to the company value.
        Example: -0.05 = -5%
        """
        self.market_cap *= (1 + percent_change)

    def apply_growth(self, months=1):
        """
        Applies baseline growth over time.
        Growth rate is annual; converted to monthly compounding.
        """
        monthly_growth = (1 + self.growth_rate) ** (months / 12) - 1
        self.market_cap *= (1 + monthly_growth)

    def apply_volatility_shock(self, base_change):
        """
        Applies shock scaled by company volatility.
        Example: war news might be base_change = -0.10
        High volatility companies react more strongly.
        """
        adjusted_change = base_change * (1 + self.volatility)
        self.market_cap *= (1 + adjusted_change)

    def debt_stress_test(self, stress_factor):
        """
        If market stress occurs, highly leveraged companies suffer more.
        stress_factor example: 0.10 during recession
        """
        penalty = stress_factor * self.debt_ratio
        self.market_cap *= (1 - penalty)

    def __repr__(self):
        return f"{self.name} ({self.sector}) - ${self.market_cap:.2f}"
    
    def react_to_market(self, forces):
        macro = forces["macro"]
        sector = forces["sectors"].get(self.sector, 0)

        # Macro + sector influence
        percent_change = (
            macro +
            sector * (1 + self.volatility)
        )

        self.apply_market_change(percent_change)

    def update_regime(self):
        if random.random() < 0.02:
            self.regime = random.choice(["bull", "bear", "recession"])

        if self.regime == "bull":
            self.macro_trend = 0.03
            self.volatility_state = 0.01
        elif self.regime == "bear":
            self.macro_trend = -0.02
            self.volatility_state = 0.02
        elif self.regime == "recession":
            self.macro_trend = -0.05
            self.volatility_state = 0.04

    def propagate_dependencies(self, companies):
        for dep in self.dependencies:
            if companies[dep].market_cap < threshold:
                self.market_cap *= 0.95