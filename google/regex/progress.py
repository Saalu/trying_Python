import re

# Repetition Qualifiers  '*'
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(".........KEEP LEARNING.............")
# Repetition Qualifiers  '+' check one or more char before
print(re.search(r"o+l", "goldfish"))
print(re.search(r"o+l", "wooly"))
# Repetition Qualifiers  '+' check if char is include before
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))
print(".........KEEP GOING.............")

# Escaping Characters
print(re.search(r"\.com", "welcome"))

print(re.search(r"\.com", "mydomain.com"))
# form '\w' for matching chars in a word including _score
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))
