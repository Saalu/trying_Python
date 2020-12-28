"""
# repetition qualifiers
def test_func(testing):
    # regex = re.search(r"Py.*n", testing)
    regex = re.search(r"Py[a-z]*n", testing)
    regex = re.search(r"o+l", testing)  # one or more preceding letter
    regex = re.search(r"p?each", testing) # zero or one preceding letter
    return regex



print(test_func('Pygmalion'))
print(test_func('To each their own'))
print('-----seperator-----')
print(test_func('Python Programmin'))
print(test_func('goldenfish'))

"""