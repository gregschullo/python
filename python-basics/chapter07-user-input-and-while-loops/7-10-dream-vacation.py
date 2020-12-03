responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("Where is your dream vacation location? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat == 'no':
        polling_active = False

print("\nPoll Results")
for name, response in responses.items():
    print(f"{name.title()} would like to travel to {response.title()}.\n")
