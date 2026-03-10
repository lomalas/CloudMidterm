import unittest
from . import countries, currencies
from .country import Country
from .company import Company
from .currency import Currency

class TestSimulationInit(unittest.TestCase):

    def test_countries_loaded(self):
        """Ensure all 20 countries are loaded"""
        self.assertEqual(len(countries), 19, "Expected 19 countries (Baresh counted once)")

    def test_company_counts(self):
        """Ensure each country has at least one company"""
        for country in countries:
            self.assertGreater(len(country.companies), 0, f"{country.name} has no companies")

    def test_currency_exists(self):
        """Ensure all countries have a currency assigned"""
        for country in countries:
            self.assertIsInstance(country.currency, Currency, f"{country.name} has no currency")

    def test_currency_pegs(self):
        """Check that pegged currencies reference another currency"""
        self.assertEqual(currencies['ARK'].peg_to.code, 'DRV', "ARK currency not pegged correctly")
        self.assertEqual(currencies['QDR'].peg_to.code, 'DRV', "QDR currency not pegged correctly")

    def test_company_values_positive(self):
        """Ensure all company starting values are positive"""
        for country in countries:
            for company in country.companies:
                self.assertGreater(company.market_cap, 0, f"{company.name} in {country.name} has non-positive value")

    def test_country_relationships(self):
        """Check neighbors, rivals, allies are lists of strings"""
        for country in countries:
            for attr in ['neighbors','rivals','allies']:
                val = getattr(country, attr)
                self.assertIsInstance(val, list, f"{country.name}.{attr} is not a list")
                for neighbor in val:
                    self.assertIsInstance(neighbor, str, f"{country.name}.{attr} contains non-string")

if __name__ == '__main__':
    unittest.main()
