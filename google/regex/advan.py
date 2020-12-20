import re

rearrange = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Saalu, Issaka")

# print(rearrange)

print("=========Print Function======")
def rearrange_name(name):
    regex = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", name)
    if name is None:
        return "Doesn't Match!"
    return regex

print(rearrange_name('Ama, Serwaa'))
