import re 

check = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
print(check)
print('========')
#to include notation marks , then we use capturing parenthese
check = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
print(check)
print('========')
# 
email = re.sub(r"[\w.%+-]+@[\w.-]+", "REDACTED", "Received an email for go_nuts95@my.example.com")
print(email)

# back slash to indicate the position of the captured group
rearrange_name = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Saalu, Issaka")
print(rearrange_name)

