import re
result = re.search(r"aza", "plaza")
print(result)
result = re.search(r"aza", "bazaar")
print(result)
result = re.search(r"aza", "maze")
print(result)
print("......................")

#strict beginning
print(re.search (r"^x", "xenon"))
print(re.search (r"^xe", "xenon"))
print("......................")

# wildCard
print(re.search (r"p.ng", "penguin"))
print(re.search (r"p.ng", "clapping"))
print(re.search (r"p.ng", "sponge"))
print("......................")
print("......................")

# character classes
print(re.search (r"[Pp]ython", "Python"))

print(re.search (r"[a-z]way", "The end of the highway"))
print(re.search (r"cloud[a-zA-z0-9]", "cloud12"))
print(re.search (r"[^a-zA-z]", "This is a sentence with spaces."))
print(re.search (r"[^a-zA-z ]", "This is a sentence with spaces."))

print("......................")
# |
print(re.search (r"cat|dog", "I like cats."))
print(re.search (r"cat|dog", "I like dogs."))
print(".........========.............")

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

# Escaping Characters

