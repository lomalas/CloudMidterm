import json
import os
from datetime import datetime
import threading

class Snapshot:
    def __init__(self, week_number, companies, currencies):
        self.week_number = week_number
        self.timestamp = datetime.now()

        # Capture numeric state of companies
        self.companies = {
            c.name: {
                "market_cap": float(c.market_cap),
                "sector": c.sector,
                "country": c.country.name if c.country else None
            }
            for c in companies
        }

        # Capture numeric state of currencies
        if isinstance(currencies, dict):
            self.currencies = {}
            for k,v in currencies.items():
                if hasattr(v, "value"):
                    self.currencies[k] = float(v.value)
                else:
                    self.currencies[k] = float(v)
        else:
            self.currencies = {cur.code: float(cur.value) for cur in currencies}

    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump({
                'week_number': self.week_number,
                'timestamp': self.timestamp.isoformat(),
                'companies': self.companies,
                'currencies': self.currencies
            }, f, indent=4)


class SnapshotManager:
    MAX_SNAPSHOTS = 500

    def __init__(self, save_dir="snapshots"):
        self.snapshots = []
        self.lock = threading.Lock()
        self.save_dir = save_dir
        os.makedirs(save_dir, exist_ok=True)

    def capture_week(self, week_number, companies, currencies):
        snapshot = Snapshot(week_number, companies, currencies)
        with self.lock:
            self.snapshots.append(snapshot)
            if len(self.snapshots) > self.MAX_SNAPSHOTS:
                self.snapshots.pop(0)
        filename = os.path.join(self.save_dir, f"week_{week_number}.json")
        snapshot.save(filename)
        print(f"[Snapshot] Week {week_number} saved: {filename}")

    def get_snapshots(self):
        with self.lock:
            return self.snapshots[:]