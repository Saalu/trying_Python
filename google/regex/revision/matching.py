import re
# print(re.search(r"p.*ng", "Penguin", re.IGNORECASE))
# '\w*' : matches alphanumeric and __ -
# charater classes are run inside square-brackets, 
# and let us list the char we want to match is of those bracket
#print(re.search())
# print(re.search(r"[a-z]*way", "The end of the highway"))
print('-------=======--------')
# print(re.search(r'[(0-5)|(7-9)]*', '8319576042'))
print(re.search(r'\w*', '8319576042'))
