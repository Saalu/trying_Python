import re
#capturing group is grouped in branket (....)
result = re.search(r"^(\w*), (\w*)$", "Saalu, Issaka")
print(result)
print(result.groups())
print(result[2])

print("{} {}".format(result[2], result[1]))

print("-----===========-----------")

# for reuse purpose
def rearrange_name(name):
    # result = re.search(r"^(\w*), (\w*)$", name)
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
print(rearrange_name("Asiya, Mumuni"))
print(rearrange_name("Fati, Moro"))
print(rearrange_name("Hooper, Grace M."))