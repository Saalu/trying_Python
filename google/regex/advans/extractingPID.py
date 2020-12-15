import re 

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing packgage upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

result = re.search(regex, "A completely different approach [34567]")
print(result)

print("-----===========-----------")


def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return "Doesn't match"
    return result[1]
#Testing
print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))
