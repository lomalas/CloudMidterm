# simulation/narrator/agent.py

from openai import OpenAI
from simulation.narrator.models import NarrativeEvent

class NarratorAgent:

    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.memory = []

    def summarize_world(self, countries, companies, currencies):
        return {
            "avg_market_cap": sum(c.market_cap for c in companies) / len(companies),
            "countries": [
                {"name": c.name, "stability": c.stability}
                for c in countries
            ],
            "major_sectors": list(set(c.sector for c in companies))
        }

    def generate_event(self, world_state):
        prompt = f"""
You are the geopolitical economic narrator of a fictional world simulation.

Given this world state:
{world_state}

Decide if a major event occurs this week.
If so, output JSON with:

title
article
sector_impacts (percent changes)
country_impacts
currency_impacts
duration_weeks

All numeric impacts should be between -0.30 and 0.30.
Return valid JSON only.
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )

        data = response.choices[0].message.content
        return data