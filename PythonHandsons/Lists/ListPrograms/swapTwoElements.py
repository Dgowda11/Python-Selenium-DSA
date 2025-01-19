a = [10, 20, 30, 40, 50]

# Swap index 2 and 4
# a[2],a[4] = a[4],a[0]
# print(a)

temp = a[2]
a[2] = a[4]
a[4] = temp
print(a)