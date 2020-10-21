name = 'salih'
 color = 'blue'
 course = 'example'
 print(name + course)
salihexample
 course * 3
'exampleexampleexample'

 colour = 'Orange'
>>> colour[1:4]
'ran'
>>> fruits = 'Pineapple'
>>> fruits = 'Pineapple'
>>> fruits[:4]
'Pine'
>>> fruits[4:]
'apple'
>>> msg = 'I love the vay you do things'
>>> print(len(msg))
28
>>> print(msg[12])
a
>>>  print(msg[11])
 
SyntaxError: unexpected indent
>>> print(msg[11])
v
>>> new_message = msg[:11] + "w" + msg[12:]
>>> print(new_message)
I love the way you do things
>>> 

def replace_domain(email, old, new):
    	if "@" + old in email:
		index = email.index("@" + old)
		new = email[:index] + "@" + new
		return new
	return email

>>> answer = 'YES'
>>> print(answer.lower())
yes
>>> " yes ".strip()
'yes'
>>> " yes ".lstrip()
'yes '
>>> " yes ".rstrip()
' yes'
>>> 
# next lesson
>>> " yes ".strip()
'yes'
>>> " yes ".lstrip()
'yes '
>>> " yes ".rstrip()
' yes'
>>> int("123") + int("123")
246
>>> " ".join(["This", "is", "my", "name"])
'This is my name'
>>> "This is another example".split()
['This', 'is', 'another', 'example']


#More on strings
>>> price = 7.5
>>> with_tax = price * 1.09
>>> print(price, with_tax)
7.5 8.175
>>> print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
Base price: $7.50. With Tax: $8.18
>>> 

#next 
>>> def to_celcius(x):
	return (x - 32) * 5/9

>>> for x in range(0, 101, 10):
	print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

