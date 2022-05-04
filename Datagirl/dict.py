empty_dict = {}
print(empty_dict)

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of furtune that never misses"
}

print(bierce)

acme_customer = dict(first = "Wile", middle = "E", last = "Coyote")

print(acme_customer)

acme_customer = dict(first="Wile",middle="E",last="Coyote")

print(acme_customer)

lot = [ ('a','b'), ('c','d'), ('e','f') ]   
                                            # list of two-item tuples
print(dict(lot))

tol = [['a','b'], ['c','d'], ['e','f'] ]   
                                            # list of two-item lists
print(dict(tol))

los = ['ab', 'cd', 'ef' ]
                                            # list of two-character strings
print(dict(los))

tos = ('ab', 'cd', 'ef' )
                                            # tuple of two-character strings
print(dict(tos))

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
pythons['Gillian'] = 'Gerry'
                                            # To add to the above list
print(pythons)

pythons['Gillian'] = 'Henry'
                                            # To replace in the above list
print(pythons)

print(pythons['Idle'])                      # To get an item

print('Grout' in pythons )                  # To test for a key at the outset, using "in"

print( pythons.get('Torn', 'Not a python') )       # To test for a key at the outset, using "get() function" 

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
                      
print(signals.keys())                          # Get all keys with keys

print(signals.values())                     # Get all values with values()

print(signals.items())                     # Get all key-value pairs with items()

print(len(signals))                         # Get length

first = {'a': 'agony', 'b': 'bliss'}
second = {'c': 'bagels', 'd': 'candy'}

print({ **first, **second })                   # Combinning dictionaries

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)

others = {'Max': 'Gruncho', 'Howard': 'Moe'}

print(pythons.update(others))                    # Combinning dictionaries with "update()"
print(pythons)

del pythons['Max']                               # Delete an item by key with del
print(pythons)

print(len(pythons))

pythons.pop('Palin')
print(len(pythons))

print(pythons.pop('First', 'Hugo'))                # Deleting using pop()
print(len(pythons))

print(pythons.clear())                              # Delete using clear()
print(pythons)

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals                                # Assign with "="

signals['blue'] = 'confuse everyone'
print(save_signals)

original_signals = signals.copy()                     # Copy with "copy()"
# signals['blue'] = 'confuse everyone'
print(signals) 

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
signals_copy = signals.copy()
print(signals)

signals = {'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}
signals_copy = signals.copy()
print(signals)
print(signals_copy)

signals['red'][1] = 'sweat'                                # Deepcopy()
print(signals)

import copy                                                #deepcopy()

signals_copy = copy.deepcopy(signals)
print(signals)