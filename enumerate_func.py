marks = [12,54,34,64,23,75,86,8]
# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 7):
#         print("Awesome") 
#     index += 1

for index, mark in enumerate(marks, start = 1):
    print(mark)
    if(index == 6):
        print("Awesome") 
