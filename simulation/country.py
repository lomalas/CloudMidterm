class Country:
    def __init__(
        self,
        name,
        currency,
        tech,
        stability,
        neighbors,
        rivals,
        allies,
        companies=None
    ):
        self.name = name
        self.currency = currency
        self.tech = tech
        self.stability = stability
        self.neighbors = neighbors
        self.rivals = rivals
        self.allies = allies

        # Allow initialization with companies
        self.companies = companies if companies else []


        # Link each company back to this country object
        for company in self.companies:
            company.country = self