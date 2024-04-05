# tup = (1,4,5)
# print(type(tup))

# # Tuple cannot be change but list can.
# if 33 in tup:
#     print("Yes")
# else:
#     print("No")

countries = ("Nepal", "India", "Deutschland",
             "Spain", "Norway")
cnt = list(countries)
cnt.append("Austria")
cnt.pop(3)
cnt[4] = "Italy"
countries = tuple(cnt)
print(countries)
# Change the Tuple in this way
# add item => remove item => change item

countries2 = ("Finland", "France", "Russia",
              "Greenland", "Poland")
together = countries + countries2
print(together)
