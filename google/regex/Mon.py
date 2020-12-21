import re

def hide_email(email):
    regex = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDIRECTED]", email)
    if email is None:
        return "Incorrect email!"
    return regex

def rearrange_name(name):
    regex = re.sub(r"([\w .-]*),([\w .-]*)$", r"\2 \1", name)
    if name is None:
        return "Doesn't match pattern"
    return regex


print(hide_email( "Received an email from saalu@my.example.com"))
print(rearrange_name( "Halima, Issaka"))


