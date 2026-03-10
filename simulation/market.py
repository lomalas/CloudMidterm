class Market:
    def __init__(self, countries, currencies):
        self.countries = {c.name: c for c in countries}
        self.currencies = {cur.code: cur for cur in currencies}

    def apply_news_effect(self, article):
        # article = {"company_changes": {...}, "currency_changes": {...}}
        for company_name, change in article.get("company_changes", {}).items():
            for country in self.countries.values():
                for company in country.companies:
                    if company.name == company_name:
                        company.value *= (1 + change)
        for currency_code, change in article.get("currency_changes", {}).items():
            if currency_code in self.currencies:
                self.currencies[currency_code].update_value(change)
