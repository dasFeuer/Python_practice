def func1():
    try:
        l = [1,2,3,4]
        i = int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print('Index Error')
        return 0
    finally:
        print('Finally clause executed.')

x = func1()
print(x)