num = int(input("Enter first Number :"))

# Approach 1
# fact  = 1
# for i in range(1,num+1):
#         fact *= i
# print("The factorial of the NUmber is ", fact)


# Approach 2 :- Using Recursive function
def factorial(num):
    if (num ==1 or num ==1):
        return 1
    else:
        return num * factorial(num-1)

print(factorial(num))
