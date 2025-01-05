# Fibonacci number = 0,1,1,2,3,5,8  """ 0+1 = 1, 1+1 =2
#n = int(input("Enter the number :"))
num1 = 0
num2 = 1
print(num1,num2)
for i in range(2,11):
    sum = num1 + num2 # 1
    print(sum, end=",")  # 1
    num1 = num2 # 2
    num2 = sum #