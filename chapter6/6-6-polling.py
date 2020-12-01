favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

names = ['jen', 'greg', 'emily', 'wade', 'sarah']

for name, language in favorite_languages.items():
    if name in names:
        print(f"Thank you, {name.title()}, for taking the poll!")
    else:
        print(f"{name.title()}, please take the poll.") 
