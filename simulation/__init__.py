# simulation_init.py

from simulation.currency import Currency
from simulation.company import Company
from simulation.country import Country

# -------------------------------
# Classes
# -------------------------------

currencies = {}

currencies['LX'] = Currency("Lexon", "LX")
currencies['SLR'] = Currency("Sol", "SLR")
currencies['HL'] = Currency("Helion", "HL")
currencies['DRV'] = Currency("Drav", "DRV")
currencies['VLC'] = Currency("Velkar Credit", "VLC")
currencies['ARK'] = Currency("Ark", "ARK", peg_to=currencies['DRV'])
currencies['VRC'] = Currency("Varin Crown", "VRC")
currencies['SEL'] = Currency("SelCoin", "SEL")
currencies['KTM'] = Currency("Karth Mark", "KTM")
currencies['TZU'] = Currency("Tazbek Unit", "TZU")
currencies['BHP'] = Currency("Baresh Peso", "BHP")
currencies['ORT'] = Currency("Orlith Standard", "ORT")
currencies['MVA'] = Currency("Mava", "MVA")
currencies['ZRD'] = Currency("Zarethian Drachma", "ZRD")
currencies['KYT'] = Currency("Korynth Tech", "KYT")
currencies['VFL'] = Currency("Virelian Florin", "VFL")
currencies['DXM'] = Currency("DraxMark", "DXM")
currencies['NRC'] = Currency("Norvane Crown", "NRC")
currencies['QDR'] = Currency("Qandor Rial", "QDR", peg_to=currencies['DRV'])

# -------------------------------
# Country & Companies Initialization
# -------------------------------

countries = []

# 1. Lexion
countries.append(Country(
    name="Lexion",
    currency=currencies['LX'],
    tech=10,
    stability=9,
    neighbors=["Varin Republic","Draxmoor"],
    rivals=["Draxmoor"],
    allies=["Solmere Collective","Helios Pact"],
    companies=[
    Company("TitanForge Defense","Defense",310,0.25,0.06,0.35,9),
    Company("Cerebra AI Systems","AI",420,0.40,0.12,0.20,8,["OmniSteel Heavy Industries"]),
    Company("Aether Aerospace","Aerospace",260,0.30,0.08,0.40,9,["TitanForge Defense"]),
    Company("IronCore Mining","Mining",190,0.35,0.05,0.30,7),
    Company("NexaDrive Motors","Automotive",145,0.28,0.04,0.50,6,["IronCore Mining"]),
    Company("Voltrix Nuclear","Energy",175,0.20,0.05,0.45,8),
    Company("OmniSteel Heavy Industries","Heavy Industry",150,0.22,0.03,0.55,7,["IronCore Mining"]),
    Company("LexAgri Systems","Agriculture",70,0.18,0.03,0.60,5)
]
))

# 2. Solmere Collective
countries.append(Country(
    name="Solmere Collective",
    currency=currencies['SLR'],
    tech=9,
    stability=9,
    neighbors=["Lexion","Helios Pact"],
    rivals=[],
    allies=["Lexion","Norvane"],
    companies=[
    Company("IonGrid Storage","Renewables",350,0.30,0.09,0.25,8),
    Company("HelioDyne Renewables","Renewables",240,0.28,0.08,0.30,7),
    Company("Verdant BioLabs","Biotech",180,0.35,0.11,0.20,7),
    Company("EcoTransit Systems","Transportation",120,0.22,0.05,0.40,6),
    Company("GreenCore Materials","Materials",95,0.25,0.04,0.45,6)
]
))

# 3. Helios Pact
countries.append(Country(
    name="Helios Pact",
    currency=currencies['HL'],
    tech=10,
    stability=9,
    neighbors=["Solmere Collective","Lexion"],
    rivals=["Draxmoor"],
    allies=["Solmere Collective"],
    companies=[
    Company("Helios Robotics","Robotics",310,0.32,0.10,0.30,8),
    Company("Synapse Automation","Automation",220,0.30,0.08,0.35,7),
    Company("QuantumWorks Labs","Tech",400,0.42,0.13,0.18,9)
]
))

# 4. Dravosk Union
countries.append(Country(
    name="Dravosk Union",
    currency=currencies['DRV'],
    tech=6,
    stability=6,
    neighbors=["Velkar Basin","Arkenfall"],
    rivals=["Korynthia"],
    allies=["Qandor Emirate"],
    companies=[
    Company("PetroDrav Energy","Oil",220,0.38,0.04,0.50,8),
    Company("Granite Crown Mining","Mining",95,0.33,0.03,0.45,6),
    Company("DravRail Logistics","Transportation",60,0.25,0.02,0.55,5),
    Company("Borealis Drilling","Oil Services",130,0.36,0.04,0.48,7),
    Company("Union Gas Export","Gas",115,0.34,0.04,0.46,7)
]
))

# 5. Velkar Basin
countries.append(Country(
    name="Velkar Basin",
    currency=currencies['VLC'],
    tech=3,
    stability=2,
    neighbors=["Dravosk Union","Baresh Dominion"],
    rivals=[],
    allies=["Draxmoor"],
    companies=[
    Company("Velkar Energy Holdings","Oil",12,0.50,0.01,0.70,6),
    Company("Cobalt Frontier Ltd","Mining",18,0.55,0.02,0.65,6),
    Company("Basin Transport Group","Transport",9,0.45,0.01,0.75,4)
]
))

# 6. Arkenfall
countries.append(Country(
    name="Arkenfall",
    currency=currencies['ARK'],
    tech=5,
    stability=5,
    neighbors=["Dravosk Union","Baresh Dominion"],
    rivals=["Dravosk Union"],
    allies=[],
    companies=[
    Company("Arkenfall Copper","Mining",70,0.30,0.03,0.50,6),
    Company("HighPeak Steel","Steel",95,0.28,0.04,0.48,7,["Arkenfall Copper"]),
    Company("Alpine Transit Co","Transport",55,0.22,0.03,0.52,5)
]
))

# 7. Varin Republic
countries.append(Country(
    name="Varin Republic",
    currency=currencies['VRC'],
    tech=8,
    stability=7,
    neighbors=["Lexion","Karth Dominion"],
    rivals=["Karth Dominion"],
    allies=["Selvarin"],
    companies=[
    Company("SkyBridge Financial","Finance",285,0.27,0.06,0.40,8),
    Company("BlueHarbor Shipping","Shipping",140,0.29,0.05,0.45,6),
    Company("Mercury Exchange Group","Finance",125,0.25,0.05,0.38,6),
    Company("Virex Technologies","Tech",210,0.35,0.09,0.30,7),
    Company("OceanGate Insurance","Insurance",90,0.20,0.04,0.35,5)
]
))

# 8. Selvarin
countries.append(Country(
    name="Selvarin",
    currency=currencies['SEL'],
    tech=9,
    stability=9,
    neighbors=["Varin Republic","Korynthia"],
    rivals=[],
    allies=["Varin Republic","Korynthia"],
    companies=[
    Company("Selvarin Global Bank","Finance",250,0.22,0.05,0.30,8),
    Company("Haven Asset Management","Finance",175,0.24,0.05,0.32,7),
    Company("SecureVault Holdings","Finance",120,0.20,0.04,0.28,6)
]
))

# 9. Karth Dominion
countries.append(Country(
    name="Karth Dominion",
    currency=currencies['KTM'],
    tech=5,
    stability=5,
    neighbors=["Varin Republic","Tazbek Industrial Zone"],
    rivals=["Varin Republic"],
    allies=[],
    companies=[
    Company("KarthWorks Manufacturing","Manufacturing",110,0.33,0.03,0.55,6),
    Company("NovaConstruct Infrastructure","Construction",95,0.30,0.03,0.60,6),
    Company("EastWeave Textiles","Textiles",45,0.40,0.02,0.65,4),
    Company("Dominion Plastics","Plastics",60,0.38,0.02,0.62,5),
    Company("UrbanRise Development","Development",70,0.35,0.03,0.58,5)
]
))

# 10. Tazbek Industrial Zone
countries.append(Country(
    name="Tazbek Industrial Zone",
    currency=currencies['TZU'],
    tech=4,
    stability=6,
    neighbors=["Karth Dominion","Baresh Dominion"],
    rivals=["Karth Dominion"],
    allies=[],
    companies=[
    Company("PolyChem Tazbek","Plastics",65,0.37,0.03,0.60,5),
    Company("Threadline Textiles","Textiles",38,0.42,0.02,0.70,4),
    Company("SunPort Assembly","Electronics",72,0.36,0.04,0.55,6),
    Company("HarborLight Exports","Shipping",50,0.30,0.03,0.58,5)
]
))

# 11. Baresh Dominion
countries.append(Country(
    name="Baresh Dominion",
    currency=currencies['BHP'],
    tech=3,
    stability=3,
    neighbors=["Tazbek Industrial Zone","Arkenfall","Velkar Basin"],
    rivals=[],
    allies=[],
    companies=[
    Company("Baresh Textiles","Textiles",25,0.45,0.01,0.75,3),
    Company("IronHands Tooling","Manufacturing",40,0.40,0.02,0.70,4),
    Company("Port Baresh Logistics","Shipping",30,0.38,0.02,0.72,4)
]
))

# 12. Orlith Strait Authority
countries.append(Country(
    name="Orlith Strait Authority",
    currency=currencies['ORT'],
    tech=6,
    stability=9,
    neighbors=["Mavaria","Zarethia"],
    rivals=[],
    allies=["Varin Republic","Lexion"],
    companies=[
    Company("Orlith Canal Corporation","Transport",300,0.20,0.05,0.35,10),
    Company("StraitShield Maritime Security","Defense",110,0.28,0.04,0.40,8),
    Company("Orlith Port Holdings","Shipping",95,0.25,0.04,0.38,7)
]
))

# 13. Mavaria
countries.append(Country(
    name="Mavaria",
    currency=currencies['MVA'],
    tech=3,
    stability=3,
    neighbors=["Orlith Strait Authority","Velkar Basin"],
    rivals=["Velkar Basin"],
    allies=[],
    companies=[
    Company("GoldenFields Agro","Agriculture",28,0.42,0.02,0.65,4),
    Company("MavaRail Freight","Transport",15,0.40,0.01,0.75,3),
    Company("AgriNova Fertilizers","Agriculture",40,0.35,0.02,0.60,5),
    Company("HarvestBond Commodities","Agriculture",22,0.38,0.02,0.68,4)
]
))

# 14. Zarethia
countries.append(Country(
    name="Zarethia",
    currency=currencies['ZRD'],
    tech=6,
    stability=8,
    neighbors=["Orlith Strait Authority"],
    rivals=[],
    allies=[],
    companies=[
    Company("Zarethia Resorts","Tourism",85,0.30,0.05,0.45,6),
    Company("AzureAir Travel","Transport",75,0.32,0.04,0.50,6),
    Company("Sapphire Coast Holdings","Luxury Goods",60,0.28,0.04,0.48,5)
]
))

# 15. Korynthia
countries.append(Country(
    name="Korynthia",
    currency=currencies['KYT'],
    tech=9,
    stability=6,
    neighbors=["Selvarin","Draxmoor"],
    rivals=["Dravosk Union"],
    allies=["Selvarin"],
    companies=[
    Company("Korynthia Cloud Systems","Tech",280,0.38,0.11,0.25,8),
    Company("NanoSpark Innovations","Tech",210,0.40,0.12,0.22,8),
    Company("CircuitWave Electronics","Tech",150,0.34,0.09,0.30,7)
]
))

# 16. Virelia
countries.append(Country(
    name="Virelia",
    currency=currencies['VFL'],
    tech=6,
    stability=8,
    neighbors=["Draxmoor","Karth Dominion"],
    rivals=["Draxmoor"],
    allies=[],
    companies=[
    Company("Virelia Grain Co","Agriculture",75,0.26,0.03,0.50,5),
    Company("SunHarvest Oils","Agriculture",60,0.25,0.03,0.52,5),
    Company("GreenPasture Livestock","Agriculture",50,0.24,0.03,0.55,4)
]
))

# 17. Draxmoor
countries.append(Country(
    name="Draxmoor",
    currency=currencies['DXM'],
    tech=7,
    stability=6,
    neighbors=["Lexion","Korynthia","Virelia"],
    rivals=["Lexion","Virelia"],
    allies=["Velkar Basin"],
    companies=[
    Company("Draxmoor Arms","Defense",190,0.35,0.05,0.45,9),
    Company("BlackForge Machinery","Manufacturing",130,0.32,0.04,0.50,7),
    Company("IronWall Logistics","Transport",85,0.28,0.03,0.48,6)
]
))

# 18. Norvane
countries.append(Country(
    name="Norvane",
    currency=currencies['NRC'],
    tech=8,
    stability=9,
    neighbors=["Solmere Collective"],
    rivals=[],
    allies=["Solmere Collective","Helios Pact"],
    companies=[
    Company("FrostCore Minerals","Mining",140,0.27,0.04,0.42,6),
    Company("PolarWind Energy","Energy",115,0.25,0.05,0.38,6),
    Company("Norvane Logistics","Transport",90,0.23,0.04,0.40,5)
]
))

# 19. Qandor Emirate
countries.append(Country(
    name="Qandor Emirate",
    currency=currencies['QDR'],
    tech=7,
    stability=8,
    neighbors=["Dravosk Union"],
    rivals=[],
    allies=["Dravosk Union"],
    companies=[
    Company("Qandor National Oil","Oil",260,0.36,0.04,0.48,9),
    Company("DesertSky Airlines","Transport",95,0.32,0.05,0.45,6),
    Company("Sovereign Capital Holdings","Finance",180,0.28,0.05,0.35,7)
]
))

# 20. Baresh Dominion (already defined as #11)
# No new entry

# -------------------------------
# Verification
# -------------------------------
'''
print(f"Loaded {len(countries)} countries with currencies and companies.")

for c in countries[:3]:
    print(f"\nCountry: {c.name}, Currency: {c.currency.code}")
    for comp in c.companies:
        print(
            f" - {comp.name} | Sector: {comp.sector} | "
            f"Market Cap: ${comp.market_cap:.2f}B | "
            f"Volatility: {comp.volatility} | "
            f"Debt: {comp.debt_ratio}"
        )
'''