# This code extends 6-10-favorite-numbers.py to make it more complex and improve output

favorite_numbers = {
    'greg': [4, 5, 99],
    'emily': [28, 30],
    'linus': [11, 4, 17, 31],
    'sara': [100, 200],
    'andrew': [74, 6, 527],
    'gus':[],
    'jenny': [22, 5, 9],
    'kerri': [42],
    'sarah': [7, 12, 56],
    'buddy': [1],
    'wade': [],
}

for person, numbers in favorite_numbers.items():
    if len(numbers) == 0:
        print(f"{person.title()} has no favorite numbers!")
        print('\n')
    elif len(numbers) == 1:
        print(f"{person.title()}'s favorite number is:")
        for number in numbers:
            print(number)
        print('\n')
    else:
        print(f"{person.title()}'s favorite numbers are:")
        for number in numbers:
            print(number)
        print('\n')
