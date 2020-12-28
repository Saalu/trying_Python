import re
# Regex in action
def test_func(testing):
    regex = re.search(r"[a-zA-Z]{5}", testing)
    regex = re.search(r"\w{5,10}", testing)
    regex = re.findall(r"\b[a-zA-Z]{5,10}\b", testing)
    
    return regex


print(test_func('a scary ghost appeared'))
print('-----seperator-----')
print(test_func('I really like strawberries'))
