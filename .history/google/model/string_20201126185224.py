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

print('saalu@example.com', '@example', '@gmail')