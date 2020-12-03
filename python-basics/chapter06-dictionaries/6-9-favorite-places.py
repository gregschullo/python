favorite_places = {
    'greg': {
        'place1': 'bozeman',
        'place2': 'duluth',
        'place3': 'spooner',
    },
    'emily': {
        'place1': 'bozeman',
        'place2': 'norman',
        'place3': 'three forks',
    },
    'sammi': {
        'place1': 'minneapolis',
        'place2': 'madison',
        'place3': 'spooner',
    },
}

for person, place in favorite_places.items():
    print(f"Person: {person.title()}")
    places = f"{place['place1'].title()}, {place['place2'].title()}, and {place['place3'].title()}"
    print(f"\t Favorite Places: {places}")
    