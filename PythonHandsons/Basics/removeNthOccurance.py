
lst  = ["geeks", "for", "geeks"]
words = "geeks"
count  = 0

for char in range(len(lst)):
    if lst[char] == "geeks":
        count += 1
        if count > 1:
            lst.pop(char)
print(lst)
