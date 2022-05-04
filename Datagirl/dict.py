empty_dict = {}
print(empty_dict)

bierce = {
    "day": "A period of twenty_four hours mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses"
}

acme_customer = dict(first="Wile", second="E", last="Coyote")

print(acme_customer)

lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}

print(pythons)

pythons['Gilliam'] = 'Gerry'
print(pythons)

pythons['Gilliam'] = 'Terry'
print(pythons)

print('Groucho' in pythons)

print(pythons.get('Cleese'))
