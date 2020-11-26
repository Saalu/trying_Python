# file = open('spider.txt')
# print(file.readline())
# print(file.read())

# file.close()

# with open("spider.txt") as file:
#     print(file.readline())


# lesson 2
with open("C:\\Users\\Saalih\\spider.txt") as file:
    for line in file:
        print(line.upper())


# with open("spider.txt") as file:
#     for line in file:
#         # print(line.strip().upper())

# file = open("spider.txt")

lines = file.readlines()
file.close()
lines.sort()
# print(lines)

# lesson 3
with open("novel.text", "w") as file:
    file.write("I am having fun coding with Python")

