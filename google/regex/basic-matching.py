import re
result = re.search(r"aza", "plaza")
print(result)
result = re.search(r"aza", "bazaar")
print(result)
result = re.search(r"aza", "maze")
print(result)
print("......................")

print(re.search (r"^x", "xenon"))
print(re.search (r"^xe", "xenon"))
print("......................")

print(re.search (r"p.ng", "penguin"))
print(re.search (r"p.ng", "clapping"))
print(re.search (r"p.ng", "sponge"))
