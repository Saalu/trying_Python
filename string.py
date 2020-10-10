name = 'Saalu'
age = 32

# === Concatenate ===
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# ==== String Formatting ===

# --Arguments by postion
# print('My name is {name} and I amd {age}'.format(name=name, age=age))

# --F-Strings (3.6+)
# print(f'Hi guys, I am {name} and I am {age}')

# === String Methods ===
s = 'hello world'

# --Capitalize string
print(s.capitalize())

# --make all uppercase
print(s.upper())

# --make all lower
print(s.lower())

# --swap case
print(s.swapcase())

# --Get length
print(len(s))

# --Replace
print(s.replace('World', 'everyone'))
print(s)
# --Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Find position
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
