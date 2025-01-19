lst = ["apple","mango","bananna"]
for x in lst:
    print(x)
print()
# Only if you use range function you need to use the indx number
for x in range(len(lst)):
    print(lst[x])
print()
i = 0
while i < len(lst):
    print(i)
    i += 1

print()
[print(x) for x in lst]