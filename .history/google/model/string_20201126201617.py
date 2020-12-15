fruit = 'Pineapple'
print(fruit[:4])
print(fruit[4:])


# test
message = 'A dong string with a typo'

new_msg = message[:2] + 'l' + message[3:]

print(new_msg)

# next

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

# print(replace_domain('saalu@example.com', '@example', '@gmail'))

test = 'Mountain'
print(test.upper())
print(test.lower())

rate = ['this', 'is', 'my', 'hommy']
print(" ".join(rate))

now = 'this how we use string'
print(now.split())

# Formatting Strings
name = 'Saalu'
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

print('Your lucky number is {number}, {name}'.format(name=name, number=len(name) *3))


price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print('Base price: ${:.2f}. With Tax: ${:.2f}'.format(price, with_tax))

def to_celsius(x):
    return (x-32)

for x in range(0, 101, 10):
    print("{:>3} F : {:>6.2f} C".format(x, to_celsius(x)))


