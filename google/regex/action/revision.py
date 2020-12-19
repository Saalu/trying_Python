import re

# ========= Capturing Groups =============
def rearrange(name):
    # result = re.search(r"^(\w*), (\w*)$", name)
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result is None :
        return name
    return "<{}> : <{}>".format(result[2], result[1])

print(rearrange("Saalu, Issaka"))
print(rearrange("Saalu, Issaka M."))
print("========New_Lesson2========")

# ========= Repetition Qualifiers =============
print( re.search(r"[a-zA-z]{5}", 'I love young girls boobs'))
print( re.findall(r"\b[a-zA-z]{5}\b", 'I love young girls boobs and spreading the thing'))
print( re.findall(r"\w{6,10}", 'I love young girls boobs and spreading the_thingna'))
print( re.findall(r"v\w{,7}", 'I love young girls boobs and parading varandasing spreading the_thingna'))
print("========New_Lesson3========")

# ========= Repetition Qualifiers =============
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing packgage upgrade"

def extract_pid(log_line):
    pattern = r"\[(\d+)\]"
    result = re.search(pattern, log_line)
    if result is None:
        return "Doesn't Match!!!"
    return result

print(extract_pid(log))
print(extract_pid("99  mycomputer bad_process[novice]"))
print("========New_Lesson4========")


# =========Split Replace =============
capture = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Saalu, Issaka")
print(capture)

