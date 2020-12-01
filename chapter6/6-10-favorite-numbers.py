favorite_numbers = {
    'greg': [4, 5, 99],
    'emily': [28, 30],
    'linus': [11, 4, 17, 31],
    'sara': [100, 200],
    'andrew': [74, 6, 527],
}

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)
    print('\n')