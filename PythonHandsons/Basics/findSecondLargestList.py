my_list = [12, 45, 2, 41, 31, 10, 8, 6, 4]

largest = my_list[0]
second_largest = None
for num in my_list[1:]:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)