import json
import os
from datetime import datetime

class Snapshot:
    def __init__(self, week_number, companies, currencies):
        self.week_number = week_number
        self.timestamp = datetime.now()

        # Capture the state of each company
        self.companies = {
            c.name: {
                "market_cap": c.market_cap,
                "sector": c.sector,
                "country": c.country.name if c.country else None
            }
            for c in companies
        }

        # Capture the state of each currency
        self.currencies = {
            cur.code: cur.value for cur in currencies
        }

    def save(self, filename):
        """Save this snapshot to a JSON file."""
        with open(filename, 'w') as f:
            json.dump({
                'week_number': self.week_number,
                'timestamp': self.timestamp.isoformat(),
                'companies': self.companies,
                'currencies': self.currencies
            }, f, indent=4)
    


class SnapshotManager:
    def __init__(self, save_dir="snapshots"):
        self.snapshots = []
        self.save_dir = save_dir
        os.makedirs(save_dir, exist_ok=True)

    def capture_week(self, week_number, companies, currencies):
        snapshot = Snapshot(week_number, companies, currencies)
        self.snapshots.append(snapshot)
        # Save automatically
        filename = os.path.join(self.save_dir, f"week_{week_number}.json")
        snapshot.save(filename)
        print(f"[Snapshot] Week {week_number} saved: {filename}")
    
    