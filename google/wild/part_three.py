# Wild Cards
import re

# Regex in action
def test_func(testing):
    regex = re.search(r"^(\w*), (\w*)$", testing)
    regex = re.search(r"^([\w .-]*), ([\w .-]*)$", testing)
    if regex is None:
        return testing
    return "{} {}".format(regex[2], regex[1])


print(test_func('Saalu, Issaka G.'))
print('-----seperator-----')
print(test_func('_this_is_a_valid_pattern'))
