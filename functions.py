def add(a, b):
    num = a + b
    print("The sum is:", num)

add(1, 3)

def avg(*num):
    # print(type(num))
    sum = 0
    for i in num:
        sum =+ i
        # print("Average is:", sum/len(num))
        # return 7
    return sum/ len(num)


avg(4, 8)

b = avg(2,4,5,6)
print(b)