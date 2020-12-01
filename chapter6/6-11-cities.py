cities = {
    'bozeman': {
        'country': 'united states',
        'population': 70000,
        'fact': 'current city',
    },
    'spooner': {
        'country': 'united states',
        'population': 2500,
        'fact': 'hometown',
    },
    'duluth': {
        'country': 'united states',
        'population': 100000,
        'fact': 'college town',
    },
}

for city, info in cities.items():
    print(f"City: {city.title()}")
    country = f"{info['country'].title()}"
    population = f"{info['population']}"
    fact = f"{info['fact']}"
    print(f"\t {country}, {population}, {fact}")
