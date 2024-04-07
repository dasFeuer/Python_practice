# Set doesn't take repeated value

# s = {2,3,1,2,3}
# print(s)

# info = {"Jack", 12, True, 7.9, 21}
# print(info)

# a = set()
# print(type(a))

# for value in info:
#     print(value)

s1 = {1,3,5,7}
s2 = {1,8,2}

# print (s1.union(s2))
# s1.update(s2)
# # print (s1.intersection(s2)
# s1.intersection_update(s2)

c1 = {"Kathmandu", "Hamburg", "Paris", "Barcelona"}
c2 = {"Hamburg", "New York", "Dehli"}
c3 = c1.difference(c2)
print(c3)
print(c1.isdisjoint(c2))
print(c1.issuperset(c2))
c1.add("Helsinki")
print(c1)
# c1.remove("Tokyo") --> Throws error
c1.discard("Tokyo") # doesn,t throw erroe

item = c1.pop()
print(c1)
print(item)

# del c1
# print(c1)

# c1.clear()

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present")
else:
    print("Carla is absent")

