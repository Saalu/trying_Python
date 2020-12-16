import re

"""
#one or more occurance of the chars
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
#one or zero occurance of the chars
print(re.search(r"p?each", "To each girl my love goes"))

print("======---------Escaping Chars------------======")
print(re.search(r"\@[a-zA-Z.]+", "saalu@gmail.com"))

pattern = r"^[a-zA-Z_ ][a-zA-Z0-9_ ]*$"
print(re.search(pattern, "_this_is_valid_name"))
print(re.search(pattern, "It is valid name"))

print("======---------Capturing Groups ()------------======")

def rearrange_name(name):
    # result = re.search(r"^(\w*), (\w*)$", name)
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Nancy, Adjei"))
print(rearrange_name("Amina, Musah H."))
"""

"""
print("======---------More on Repetition Qualifiers------------======")
print(re.search(r"[a-zA-Z]{4}", "I love to marry but I don't have the need"))
print(re.findall(r"[a-zA-Z]{4}", "I love to marry but I don't have the need"))
# if we want exact word as specified
print(re.findall(r"\b[a-zA-Z]{4}\b", "I love to marry but I don't have the need"))
# range from lower to upper limit
print("--------watch out ---------")
print(re.findall(r"\b\w{5,10}\b", "I love to marry beautified but I don't have the need"))

# from zero to that num of specified
print(re.search(r"p\w{5,}", " I like to travel the world programming_life"))
print(re.search(r"p\w{,10}", " I like to travel the world programming"))

print("======---------Extracting PID ------------======")
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing packgage upgrade"

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return "Not Fund"
    return result[1]

print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))
"""

print("======---------Split and Replacing ------------======")
trying = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
trying = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
print(trying)

print("======---------Continue ------------======")
substitute = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Receive for imma@my.example.com")
rename = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Flippo, Santo")
print(substitute)
print(rename)

