s = "Hello world"
s2 = ""

# for char in s:
#     if char != 'o':
#         s2 += char
# print(s2)

# USing list COmprehension
a = "".join([c for c in s if c != "o"])
print(a)