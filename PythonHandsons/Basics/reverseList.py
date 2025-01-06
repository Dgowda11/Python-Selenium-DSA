lst = [2,4,6,8,10,12,14,16,18]
# Using Reverse Method  --1
lst.reverse()
print(lst)

# Using Slicing Method  --1
rev = lst[::-1]
print(rev)

# Using for loop and range Function --3
rev_lst = []
for i in range(len(lst)-1,-1,-1):
    rev_lst.append(lst[i])

print(rev_lst)