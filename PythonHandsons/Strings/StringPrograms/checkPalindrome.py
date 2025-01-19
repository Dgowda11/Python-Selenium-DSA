# def is_palindrome(String):
#     string  = String.lower()
#     for i in range(len(string) // 2):
#         if string[i] != string[len(string) - i -1]:
#             return False
#     return True


# if is_palindrome("Madam"):
#     print("Its a Palindrome")
# else:
#     print("Not a palindrome")

Str1  = "Madam"
Str1 = Str1.lower()
str2 = Str1[::-1]
print(str2)
if Str1 == str2:
    print("Plaindrome")
else:
    print("Not a Palindorme")
