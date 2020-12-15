import re
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))
print('--------=======--------')

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "thi isn't valid"))
print(re.search(pattern, "_variable_name45"))
print(re.search(pattern, "33variable_name"))