# Wild Cards
import re


def test_func(testing):
    regex = re.search(r"cloud.[a-zA-Z0-9]", testing)
    regex = re.search(r"[a-zA-Z0-9].", testing)
    regex = re.findall(r"cat|dog", testing)
    return regex



print(test_func('cloud3355'))
print('-----seperator-----')
print(test_func('I like both dogs and cats'))
print(test_func('thi is my coding ground'))
