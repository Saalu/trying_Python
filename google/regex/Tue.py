import re

def rearrange_name(name):
    # regex = re.search(r"^(\w*), (\w*)$", name)
    regex = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if regex is None:
        return name
    return "{} - {}".format(regex[2], regex[1])

print(rearrange_name("Adamu, Issaka M."))

# ---------Next Lesson -------------
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))
print(re.findall(r"\b a\w{,7}\b", "a scary ghost appeared"))

# ---------Next Lesson -------------
print("=======finished=======")
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[Name_HASHED#]", 'Received and email from issaka@gmail.com'))
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Saalu, Issaka"))

