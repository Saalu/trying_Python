# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    'first_name': 'Saalih',
    'last_name': 'Ishaq',
    'age': 30
}

# use constructor
# person2 = dict(first_name='Fati', last_name='Umar')

print(person, type(person))

# Get value
print(person['first_name'])
print(person.get('age'))

# Add key/value
person['phone'] = '345-659-659'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
# person2['city'] = 'Boston'

print(person2)

# Remove item
del (person['age'])
# person.pop('phone')


# Clear
person.clear()


# list of dict
people = [
    {'name': 'Kelvin', 'age': 25},
    {'name': 'Gabby', 'age': 33}
]

print(people[1]['name'])
