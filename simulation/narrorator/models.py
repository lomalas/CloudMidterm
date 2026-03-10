# simulation/narrator/models.py

from dataclasses import dataclass
from typing import Dict

@dataclass
class MarketConditions:
    sentiment: float          # -1 to +1
    volatility: float         # 0 to 1
    geopolitical_tension: float
    liquidity: float

@dataclass
class NarrativeEvent:
    title: str
    article: str
    sector_impacts: Dict[str, float]
    country_impacts: Dict[str, float]
    currency_impacts: Dict[str, float]
    duration_weeks: int