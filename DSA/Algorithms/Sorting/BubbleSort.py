def bubble_sort(my_lst):
    for i in range(len(my_lst) -1 , 0 , -1):
        for j in range(i):
            if my_lst[j] > my_lst[j+1]:
                temp = my_lst[j]
                my_lst[j] = my_lst[j+1]
                my_lst[j+1] = temp
    return my_lst

lst = [50,23,45,66,78,21,45]
print(lst)
print("List after Sorting. !")
print(bubble_sort(lst))