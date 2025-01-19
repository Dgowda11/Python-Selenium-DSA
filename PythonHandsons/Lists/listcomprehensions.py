# Creating new list without list comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_lst  = []
#
# for x in fruits:
#     if "a" in x:
#         new_lst.append(x)
# print(new_lst)

# Same using the list comph
# fruits = [x for x in fruits if "a" in x]
# print(fruits)
# z = [x for x in range(10)]
# print(z)


# New list whihc accept only number less than 5

lst = [x for x in range(10) if x < 5 ]
print(lst)


