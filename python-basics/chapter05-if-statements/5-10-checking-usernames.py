current_users = ['ADMIN', 'Greg', 'Emily', 'Gunner', 'Linus']
new_users = ['Greg', 'Emily', 'Callie', 'Ziggy', 'Sammy']

current_users = [users.lower() for users in current_users]
new_users = [users.lower() for users in new_users]

for new_user in new_users:
    if new_user in current_users:
        print("Sorry, that username is taken. Please select a new username.")
    else:
        print(f"Welcome {new_user.title()}!")
