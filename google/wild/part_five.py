import re
# Regex in action
def test_func(testing):
    regex = re.search(r"[a-zA-Z]{5}", testing)
    regex = re.search(r"\w{5,10}", testing)
    regex = re.findall(r"[.?!]", testing)
    regex = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", testing)
    
    return regex


print(test_func('a scary ghost appeared'))
print('-----seperator-----')
print(test_func('Albert, Wondila'))
