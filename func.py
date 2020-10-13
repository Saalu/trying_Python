def greeting(name, dept):
    print('Welcome, ' + name + ', You are part of ' + dept)
    # print('You are part of ' + dept)


greeting('Saaleh', 'IT Support')

# Return Values


def getSum(x, y):
    total = x + y
    return total


num = getSum(3, 4)
# print(num)

# getSum = lambda num1, num2: num1 + num2

# print(getSum(10,15))

# calculating the area of a triangle


def area_triangle(base, height):
    return base*height/2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b
print("The sum of both areas is; " + str(sum))


def convert_secs(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


hours, minutes, seconds = convert_secs(5000)
print(hours, minutes, seconds)
