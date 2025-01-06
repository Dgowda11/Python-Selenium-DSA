
input = input("Enter the String :")
# rev = input[::-1]
# if rev == input:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


def is_Plaindrome(string):
    string  = string.lower()

    length = len(string)

    for i in range(len(string) // 2):
        if string[i] != string[length -i -1]:
            return False
        return True

if is_Plaindrome(input):
    print("Its a Palindrome")
else:
    print("Not a Palindrome")