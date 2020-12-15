import re

print(re.search(r"[a-zA-Z]{5}", "a ghost"))
# to print all match search
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))

print("-----===========-----------")

# to print all match search between a range {5,10}
print(re.findall(r"\w{5,10}", "I really like strawberries"))

# to print all match search between a range {5,10} STRICT-MATCH  \b()\b
print(re.findall(r"\b(\w{1,4})\b", "I really like strawberries"))

# to print all match with beginning of r 
print(re.findall(r"r\w{,4}", "I really like strawberries"))
# to print all match with beginning of s 
print(re.findall(r"s\w{,20}", "I really like strawberries"))
