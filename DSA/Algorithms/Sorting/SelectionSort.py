def selection_Sort(my_lst):
    for i in range(len(my_lst)-1):
        min_index = i
        for j in range(i+1, len(my_lst)):
            if my_lst[j] < my_lst[min_index]:
                min_index = j
        if i != min_index:
            temp = my_lst[i]
            my_lst[i] = my_lst[min_index]
            my_lst[min_index] = temp
    return my_lst

print(selection_Sort([2,6,4,1,9,11,67,23]))