def insertion_sort(my_lst):
    for i in range(1,len(my_lst)):
        temp  = my_lst[i]
        j = i-1
        while temp < my_lst[j] and j > -1:
            my_lst[j+1] = my_lst[j]
            my_lst[j] = temp
            j -= 1
    return my_lst

print(insertion_sort([4,2,1,6,4,9,11,45]))