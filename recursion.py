def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))

num = int(input("Enter the number for factorial:"))
print("Number:", num)
print("Factorial:", factorial(num))