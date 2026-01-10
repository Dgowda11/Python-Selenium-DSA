expenses = [1200,1500,1300,1700]
# calculate the total expense
total = 0
for exp in expenses:
    total = total + exp
print(total)


# break
key_location="chair"
locations = ["sofa","garage","chair","table","closet"]

for loc in locations:
    if loc == key_location:
        print("Key location found at:", loc)
        break
    else:
        print("Key loc not found in:",loc)


# continue: print odd numbers between 1 to 10
for i in range(11):
    if i % 2 == 0:
        continue
    print(i)


# While loop 
num = 0
while num < 10:
    print(num)
    num += 1