# Wild Cards
import re

# Regex in action
def test_func(testing):
    # regex = re.search(r"\.com", testing)
    regex = re.search(r"\w*", testing) # zero or one preceding letter
    regex = re.search(r"^[a-zA-Z_][a-zA-Z0-9]*$", testing) # zero or one preceding letter
    return regex


print(test_func('welcome'))
print('-----seperator-----')
print(test_func('_this_is_a_valid_pattern'))
