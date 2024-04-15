import operator

num1 = 1
num2 = 2

sum = operator.add(num1,num2)
print(f"sum of {num1} and {num2} is {sum}")


addNum = lambda x, y: x + y

num1 = 4
num2 = 6

result = addNum(num1, num2)

print(f"sum of {num1} and {num2} is {result}")


def add (c, d):
    if d == 0:
        return c
    else:
        return add(c + 1, d -1)

num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))

res = add(num1, num2)

print(f"sum of {num1} and {num2} is {res}")



