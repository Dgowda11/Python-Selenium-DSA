lst = [2,3,4,2,4,6,22,34,21,55,65,34,76,21]
# mini = lst[0]
# maxi = lst[0]
#
# for i in range(len(lst)):
#     if lst[i] > maxi:
#         maxi = lst[i]
#     if lst[i] < mini:
#         mini = lst[i]

lst.sort()
print(lst)
print("The Maximum number of the list is :", lst[0])
print("The Minimum number of the list is :", lst[-1])