import threading
import time

from simulation.market_tick import update_companies, update_currencies


class SimulationController:

    def __init__(self, companies, currencies, snapshot_manager):

        self.companies = companies
        self.currencies = currencies
        self.snapshot_manager = snapshot_manager

        self.running = False
        self.week = 0

        self.thread = threading.Thread(target=self.loop)
        self.thread.daemon = True
        self.thread.start()

    def loop(self):

        while True:

            if self.running:

                update_companies(self.companies)
                update_currencies(list(self.currencies.values()))

                self.snapshot_manager.capture_week(
                    self.week,
                    self.companies,
                    self.currencies
                )

                self.week += 1

            time.sleep(1)

    def play(self):
        self.running = True
        print("[Controller] Simulation started")

    def pause(self):
        self.running = False
        print("[Controller] Simulation paused")

    def reset(self):

        self.running = False
        self.week = 0

        self.snapshot_manager.clear()

        print("[Controller] Simulation reset")

    def status(self):

        return {
            "running": self.running,
            "week": self.week,
            "snapshots": len(self.snapshot_manager.get_snapshots())
        }