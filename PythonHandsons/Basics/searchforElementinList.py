n = int(input("Enter the Element :"))

char_idx = 0
found = False
lst = [2,4,6,8,10,12,14,16,18]
for i in range(len(lst)):
    if n == lst[i]:
        found = True
        char_idx = i
if found:
    print(f"{n} Found at the Index of {char_idx}")
else:
    print(f"{n} Not Found")