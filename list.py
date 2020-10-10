# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
numbers = [1, 2, 3, 4, 5]

fruits = ['Apples', 'Oranges', 'Pears']
# print(numbers, num2)

# get value
print(fruits[1])

# get length
print(len(fruits))

# append to list
fruits.append('Mangoes')

# change value
fruits[0] = 'coconut'
# remove from list
fruits.remove('Pears')

# Insert into position
fruits.insert(2, 'Strawberries')

# remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)
